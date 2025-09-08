Blackbox Testing JPTEUNM (ISO25010)

Local run:
1. python -m venv .venv
2. .\.venv\Scripts\Activate
3. pip install -r requirements.txt
4. python tests/functional/test_homepage.py

Performance & security require Docker:
- k6: docker run --rm -v ${PWD}:/work -w /work loadimpact/k6 run tests/performance/perf_test.js
- ZAP: docker run -t --rm owasp/zap2docker-stable zap-baseline.py -t https://jpteunm.com -r zap_report.html
