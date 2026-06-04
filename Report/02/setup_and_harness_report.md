# Report 02 — PRD · Harness · Rules · Git

| 항목 | 내용 |
|------|------|
| 프로젝트 | MagicSquare_xx |
| 단계 | STEP 1 후속 — 문서·골격·규칙·원격 저장 |
| 브랜치 | `spec` (작업), `main` (PRD만) |
| 작성일 | 2026-06-04 |
| 상태 | Harness 골격 완료 / 구현·테스트 본문 미착수 |

---

## 1. 작업 요약

| 순서 | 작업 | 산출물 |
|------|------|--------|
| 1 | Mom Test 결과 반영 PRD | `docs/PRD.md` |
| 2 | GitHub 초기 업로드 | `main` @ `c45f728` |
| 3 | `spec` 브랜치 생성 | Harness 작업 브랜치 |
| 4 | ECB + Dual-Track TDD Harness | `pyproject.toml`, `src/`, `tests/` |
| 5 | GitHub 전 브랜치 push | `main`, `spec` @ `81e285e` |
| 6 | Cursor Rules 초안 | `.cursorrules` |
| 7 | 본 보고서·transcript | `Report/`, `export/` |

## 2. 저장소

- **URL**: https://github.com/kongkeonpyo-kr/MaginSquare_xx.git
- **인증**: 로컬 Git Credential Manager (`credential.helper = manager`) — 채팅 토큰 불필요

### 브랜치·커밋

| 브랜치 | 커밋 | 내용 |
|--------|------|------|
| `main` | `c45f728` | `docs/PRD.md` |
| `spec` | `81e285e` | PRD + Harness 골격 |

### 미커밋 (로컬)

- `.cursorrules`
- `Report/01/`, `Report/02/`, `export/transcript.md` (본 작성분)

## 3. Harness 구조

```
MagicSquare_xx/
├── pyproject.toml          # pytest dev 의존
├── docs/PRD.md
├── .cursorrules
├── src/
│   ├── entity/__init__.py
│   ├── control/__init__.py
│   └── boundary/__init__.py
├── tests/
│   ├── entity/__init__.py
│   ├── control/__init__.py
│   └── boundary/__init__.py
├── Report/
│   ├── 01/mom_test_report.md
│   └── 02/setup_and_harness_report.md
└── export/
    └── transcript.md
```

## 4. `.cursorrules` 핵심 (PRD 보완)

| 영역 | 규칙 |
|------|------|
| **도메인** | 4×4, 빈 칸 **정확히 2**, 1~16, MAGIC_SUM=34 |
| **출력** | `int[6]` = `[r1,c1,n1,r2,c2,n2]`, 좌표 **1-index** |
| **오류** | E001~E007 (Boundary); Entity는 E001~E005 **처리 금지** |
| **ECB** | boundary → control → entity; entity 역import 금지 |
| **Dual-Track** | Logic Mock 금지 / UI Mock 허용 |
| **테스트 ID** | D-* (Logic), U-* (UI); `test_d_*` / `test_u_*` |
| **TDD** | RED→GREEN→REFACTOR; skip/xfail/assert 완화 금지 |
| **SSOT** | `MagicConstant` — 34/16 리터럴 산재 금지 |

## 5. PRD vs `.cursorrules` 오류 코드

| PRD (초안) | `.cursorrules` |
|------------|----------------|
| E-DUP, E-OVER, E-RANGE … | E001~E007 번호 체계 |
| 구현 시 `.cursorrules` E001~E007를 SSOT로 통일 권장 |

## 6. 다음 단계 (STEP 2~)

1. `entity.MagicConstant` + Entity RED 테스트 (D-*)
2. Control `SquareValidator` — E001~E003 판정
3. Boundary 입출력 — U-* 테스트 (Mock 허용)
4. `spec` → `main` PR 또는 merge

## 7. 검증 명령 (Harness)

```powershell
cd c:\0604_AI\MagicSquare_xx
pip install -e ".[dev]"
pytest --collect-only
```

현재 테스트 본문 없음 → collected 0 expected.

## 8. 한 줄 결론

**Mom Test로 문제를 고정한 뒤, ECB·Dual-Track TDD를 받칠 최소 Harness와 AI 규칙까지 준비 완료. 구현은 RED부터 시작.**
