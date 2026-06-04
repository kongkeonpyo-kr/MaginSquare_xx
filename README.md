# MagicSquare_xx (MagicSquare_1004)

4×4 **부분 마방진** 학습 도구 — **ECB** + **Dual-Track TDD** (RED → GREEN → REFACTOR).

| 항목 | 내용 |
|------|------|
| PRD | [`docs/PRD.md`](docs/PRD.md) |
| AI 규칙 | [`.cursorrules`](.cursorrules) |
| RED 커맨드 | [`.cursor/commands/tdd-red.md`](.cursor/commands/tdd-red.md) (`/tdd-red`) |
| 원격 | https://github.com/kongkeonpyo-kr/MaginSquare_xx |

## 빠른 시작

```powershell
cd c:\0604_AI\MagicSquare_xx
pip install -e ".[dev]"
pytest --collect-only
```

## Dual-Track TDD

| Track | Layer | 테스트 파일 | ID |
|-------|-------|-------------|-----|
| Logic | entity, control | `tests/**/test_d_*.py` | **D-*** |
| UI | boundary | `tests/**/test_u_*.py` | **U-*** |

**RED** 작업 시 Cursor에서 `/tdd-red`를 사용하고, 응답 첫 줄에  
`Phase: red | Layer: ... | Track: ...` 를 선언합니다.  
상세 절차·금지 사항은 [tdd-red.md](.cursor/commands/tdd-red.md)를 따릅니다.

```bash
pytest tests/entity/test_d_*.py::test_name -x   # Logic
pytest tests/boundary/test_u_*.py::test_name -x  # UI
```

## 프로젝트 구조

```
MagicSquare_xx/
├── src/
│   ├── entity/
│   ├── control/
│   └── boundary/
├── tests/
│   ├── entity/
│   ├── control/
│   └── boundary/
├── docs/PRD.md
├── .cursorrules
└── .cursor/commands/tdd-red.md
```

## 브랜치

| 브랜치 | 용도 |
|--------|------|
| `main` | PRD·안정 문서 |
| `spec` | Harness·통합 작업 |
| `red` | TDD RED 단계 작업 (권장) |

---

## 할 일 체크리스트

### 환경 · 저장소

- [ ] `pip install -e ".[dev]"` 완료
- [ ] `pytest --collect-only` 실행 확인
- [ ] 작업 브랜치 `red` (또는 `spec`) 체크아웃
- [ ] `.cursorrules`, `Report/`, `.cursor/commands/` 원격 반영 (필요 시 commit·push)

### 문서 · 정책

- [ ] [Issue #3](https://github.com/kongkeonpyo-kr/MaginSquare_xx/issues/3) 브랜치 정책 검토·결정
- [ ] `docs/BRANCHING.md` (또는 CONTRIBUTING)에 브랜치 정책 반영
- [ ] PRD 오류명(E-DUP 등) ↔ `.cursorrules` E001~E007 매핑 확정

---

### RED — Logic Track (`test_d_*.py`, Mock 금지)

각 항목: **ID 확인 → AAA 테스트 → `pytest -x` FAIL** · 변경은 **`tests/`만**.

- [ ] **D-*** `MagicConstant` — `SIZE`, `MAGIC_SUM`, `MIN_VAL`, `MAX_VAL` (리터럴 34/16 금지)
- [ ] **D-*** Entity 상태·격자 계약 (4×4, 빈 칸 2개 전제)
- [ ] **D-*** `SquareValidator` — E001 범위(1~16)
- [ ] **D-*** `SquareValidator` — E002 중복
- [ ] **D-*** `SquareValidator` — E003 행·열 합 > `MAGIC_SUM`
- [ ] **D-*** `SquareValidator` — E004 빈 칸 개수 ≠ 2
- [ ] **D-*** `SquareValidator` — E005 완성 후 10줄 합·집합
- [ ] **D-*** Solver / E007 해 없음 (범위 확정 후)

RED 보고 예시 (`/tdd-red`):

```
Phase: red | Layer: entity | Track: Logic
ID: D-001 | FAIL: AttributeError — MagicConstant.SIZE 없음
files: tests/entity/test_d_magic_constant.py
```

---

### RED — UI Track (`test_u_*.py`, Control stub 허용)

| ID | Given | Then (기대) | Expected FAIL |
|----|-------|-------------|---------------|
| U-IN-01 | `grid=None` | `E003` `INVALID_NULL` | `ModuleNotFoundError` |
| U-IN-02 | `grid=3×4` | `E001` `INVALID_SIZE` | `AssertionError` |
| U-IN-03 | 빈 칸 0개 | `E002` `INVALID_BLANKS` | `AssertionError` |
| U-OUT-01 | 유효 입력 G1 | `len(result)==6` | `pytest.fail()` RED |
| U-FLOW-02 | `grid=None` | `execute()` 0회 | `pytest.fail()` RED |

- [ ] **U-IN-01** — null 입력 RED
- [ ] **U-IN-02** — 잘못된 격자 크기 RED
- [ ] **U-IN-03** — 빈 칸 0개 RED
- [ ] **U-OUT-01** — 성공 출력 `int[6]` 길이 RED
- [ ] **U-FLOW-02** — 무효 입력 시 Control 미호출 RED

RED 보고 예시:

```
Phase: red | Layer: boundary | Track: UI
ID: U-IN-01 | FAIL: ModuleNotFoundError — boundary 모듈 없음
files: tests/boundary/test_u_io.py
```

---

### RED 공통 금지 (`/tdd-red` 준수)

- [ ] RED 단계에서 `src/` 수정 없음 확인
- [ ] Logic Track Mock/patch·Fake Control 미사용
- [ ] `skip` / `xfail` / assert 완화 없음
- [ ] 현재 테스트 **pass 전** 다음 RED 추가 없음 (GREEN 게이트)

---

### GREEN · REFACTOR (RED 완료 후)

- [ ] RED 항목별 최소 구현으로 `pytest` pass (GREEN)
- [ ] REFACTOR — ECB·SSOT 정리 (snapshot 갱신은 사용자 **「승인」** 후)
- [ ] `pytest` 전체 pass (Review 게이트)
- [ ] `spec` → `main` PR (브랜치 정책·CI 준비 후)

---

## 참고

- Mom Test · Harness: [`Report/01/`](Report/01/), [`Report/02/`](Report/02/)
- 오류 코드 SSOT: E001~E007 — [`.cursorrules`](.cursorrules)
- Solver 출력: `int[6]` = `[r1,c1,n1,r2,c2,n2]` (Boundary 대외 **1-index**)
