# 아나콘다 가상환경 동기화

- 아나콘다 내용 수정 후에는 꼭 사용바람.

## 아나콘다 가상환경 .yaml로 내보내기

```bash
conda env export > environment.yaml
```

## 아나콘다 가상환경 .yaml로 불러오기

```bash
conda env create -f environment.yaml
```
