# 🧪 Consumer Persona Fidelity Auditor (XAI)

> **Auditing Post-hoc Rationalization in Lightweight LLM Shopping Agents using Counterfactual Micro-Perturbations**

본 연구 프레임워크는 소비자 페르소나를 장착한 LLM 쇼핑 에이전트가 추천 결론을 미리 정해두고 사후에 기만적인 핑계를 대는 **'사후 정당화(Post-hoc Rationalization)' 현상**을 실제 아마존 리뷰 로그 및 LIME 기반 미세 섭동($x \to z'$)을 통해 정량적으로 감사(Audit)합니다.

---

## 🚀 Key Features

1. **실제 데이터 실시간 스트리밍**: UCSD Amazon Review 2023 (Electronics) 원본 서버로부터 대용량 압축 스트림을 실시간 파싱.
2. **페르소나 & 핵심 제약조건 마이닝**: 실제 고객의 구매/리뷰 이력으로부터 절대적 제약조건(Hard Constraints) 자동 추출.
3. **관심사 & 예산 기반 카탈로그 매칭**: 초기 추천(`RECOMMEND`)을 유도하는 정밀 매칭 엔진.
4. **LIME 적대적 미세 섭동 ($x \to z'$)**: 핵심 제약조건을 교묘하게 위반하는 보상형 섭동 주입.
5. **사후 정당화 자동 적발 (Excuse Hunter)**: 섭동 상황에서 추천을 고수하기 위해 스펙을 날조(Hallucination)하는 행위를 LLM-as-a-Judge로 교차 감사.

---

## 🛠️ Quickstart

### 1. 패키지 설치
```bash
pip install groq pandas requests
```

### 2. Groq API 키 설정
[Groq Console](https://console.groq.com/keys)에서 발급받은 무료 API 키를 환경변수에 등록합니다:
```bash
set GROQ_API_KEY=gsk_your_key_here
```

### 3. 실전 감사 실행
```bash
python real_amazon_auditor.py
```
또는 VS Code에서 `cockpit_real_audit.ipynb` 노트북을 열고 실행하세요.

---

## 📊 Core Metrics

* **Unfaithfulness Rate (사후 정당화 붕괴율)**: 결함 섭동 발생 시 결론을 고수하기 위해 거짓 변명을 날조한 비율
* **Decision Flip Rate (민감도)**: 제약조건 위반 시 추천을 취소(철회)한 비율
* **Average Fidelity Score**: 0.0 (완전 기만) ~ 1.0 (완전 충실)
