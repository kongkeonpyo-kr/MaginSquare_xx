# TDD RED — 실패 테스트 먼저

MagicSquare_1004 · Dual-Track TDD · **RED 단계만** (GREEN·REFACTOR·`src/` 구현 금지)

## 필수 선언

응답 **첫 줄**:

```
Phase: red | Layer: <entity|control|boundary> | Track: <Logic|UI>
```

| Track | Layer | 파일 | ID |
|-------|-------|------|-----|
| Logic | entity, control | `tests/**/test_d_*.py` | **D-*** |
| UI | boundary | `tests/**/test_u_*.py` | **U-*** |

## 절차

1. **ID 확인** — PRD·기존 테스트와 중복 없는 **D-*** / **U-*** 부여 (함수 docstring·주석에 명시)
2. **AAA 테스트** — Arrange / Act / Assert (`tests → src` import OK, ECB 역import 금지)
3. **pytest FAIL** — 단일 테스트 `-x`로 RED 입증 (미구현·의도된 assert 실패만 유효; 오타·import 실수는 RED 아님)

## pytest 예시 (bash)

```bash
cd /path/to/MagicSquare_xx

# Logic — Entity
pytest tests/entity/test_d_magic_constant.py::test_d_001_size_is_four -x

# Logic — Control
pytest tests/control/test_d_square_validator.py::test_d_010_rejects_duplicate -x

# UI — Boundary
pytest tests/boundary/test_u_io.py::test_u_in_01_grid_none -x
```

## 보고

| 항목 | 내용 |
|------|------|
| 테스트 ID | D-*** 또는 U-*** |
| FAIL 요약 | pytest 실패 유형·메시지 1~3줄 |
| 변경 파일 | **`tests/`만** |

```
Phase: red | Layer: entity | Track: Logic
ID: D-001 | FAIL: AttributeError — MagicConstant.SIZE 없음
files: tests/entity/test_d_magic_constant.py
```

## 금지

- **`src/` 수정** — 구현은 GREEN
- **Logic Track Domain Mock** — Entity·Control `Mock`/`patch`·Fake Control 금지
- **assert 완화** — `skip`·`xfail`·느슨한 assert 금지 (사용자 **「승인」** 시만 예외)
- Logic Track에서 **boundary import**
- 테스트에 **`34`/`16` 리터럴** — `MagicConstant` SSOT 사용
