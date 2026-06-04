# [정책] 브랜치 관리 정책 수립 및 문서화

## 배경

MagicSquare_xx 저장소는 초기 설정 단계에서 `main`과 `spec` 두 브랜치로 작업이 분리되어 있습니다.  
Harness·구현·PRD가 병행되면서 **역할·머지·보호 규칙**을 명시하지 않으면 충돌·오염·되돌리기 비용이 커집니다.

## 현재 상태 (2026-06-04 기준)

| 브랜치 | 역할 (현행 관행) | 비고 |
|--------|------------------|------|
| `main` | PRD·안정 문서 | `docs/PRD.md` 중심 |
| `spec` | Harness·구현·TDD 작업 | ECB 골격, 테스트 추가 예정 |

- 원격: `main`, `spec` push 완료 (Report/02)
- 로컬 미푸시: `.cursorrules`, `Report/`, `export/` 등

## 제안: 브랜치 관리 정책

### 1. 기본 브랜치

- **Default branch**: `main`
- `main`에는 **검증된 산출물만** 반영 (PRD, 승인된 문서, GREEN 게이트 통과 코드)

### 2. 브랜치 역할

| 브랜치 | 용도 | 직접 push |
|--------|------|-----------|
| `main` | 릴리스·문서 SSOT | ❌ (PR만 권장) |
| `spec` | 기능·Harness·TDD 통합 작업 | ✅ (개인/팀 작업용) |
| `feature/*` | 단일 기능·RED→GREEN 단위 (선택) | ✅ |
| `fix/*` | 버그·규칙 수정 (선택) | ✅ |

### 3. 머지 규칙

1. **`spec` → `main`**: Pull Request 필수
2. PR 머지 전 **게이트**:
   - `pytest` 전체 pass (`.cursorrules` Review 게이트)
   - Dual-Track: Logic Track Mock 금지 준수
   - PRD·`.cursorrules`와 오류 코드(E001~E007) 불일치 시 문서 동기화
3. **`main` → `spec`**: 정책·PRD만 변경 시 rebase 또는 merge로 동기화 (정기)

### 4. 커밋·push

- `git commit` / `push`는 **작업자(또는 AI) 명시 요청 시**만 (프로젝트 규칙)
- force push to `main` **금지**

### 5. GitHub 보호 규칙 (권장 설정)

`main`에 대해:

- [ ] Require a pull request before merging
- [ ] Require status check (CI: `pytest` 추가 후)
- [ ] Restrict force pushes
- [ ] (선택) Require linear history

`spec`에 대해:

- [ ] Force push 제한 (팀 합의 시)

### 6. 문서화 TODO

- [ ] `docs/BRANCHING.md` 또는 `CONTRIBUTING.md`에 본 정책 반영
- [ ] README에 브랜치 요약 링크
- [ ] CI 워크플로 추가 시 브랜치별 트리거 정의 (`main`, `spec`, PR)

## 논의·결정 필요 사항

1. `spec`을 장기 통합 브랜치로 유지할지, `feature/*` + 짧은 수명 `spec`으로 전환할지
2. `main`에 코드 머지 시점 (STEP 2 Entity RED 완료 후 vs Boundary 완료 후)
3. GitHub Actions 도입 시점 및 필수 체크 목록

## 참고

- Report: `Report/02/setup_and_harness_report.md`
- 규칙: `.cursorrules` (TDD 게이트, commit 정책)
- 저장소: https://github.com/kongkeonpyo-kr/MaginSquare_xx
