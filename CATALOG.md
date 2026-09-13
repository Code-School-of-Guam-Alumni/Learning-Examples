# Recording and Code Migration Catalog

This is the queue for matching CSG recordings to runnable code. `README.md` lists the examples that have passed verification; this file includes work that is still in progress.

## Verified

| Area | Lesson | Recording | Code |
| --- | --- | --- | --- |
| Rails APIs | One-to-many associations | Current Cohort 3 session mapping pending; [Cohort 2 W6D5](https://www.youtube.com/watch?v=IVqzUmIdFPk) is the supporting classroom recording | [Verified Organizer API commits](rails/associations/one-to-many/README.md) |

## Next Rails API mappings

| Lesson | Recording | Candidate source |
| --- | --- | --- |
| Serializers | [Cohort 2 W7D2](https://www.youtube.com/watch?v=mbkrFwA9m-4) | Cohort 2 Rails API repositories |
| Integrated Rails API | [Cohort 2 W7D3](https://www.youtube.com/watch?v=Ugt-7pUF6l0) | `full-stack-app` and the matching backend repository |
| Many-to-many associations | [Cohort 2 W7D4](https://www.youtube.com/watch?v=aEv6D6UNd74) | Cohort 2 Rails API repositories |
| Authentication and JWT | [Cohort 2 W8D1](https://www.youtube.com/watch?v=pfSrtsnlubg) | `auth-practice-api` |
| Authorization with Pundit | [Cohort 2 W8D4](https://www.youtube.com/watch?v=umR507m_B9I) | `auth-practice-api` |
| API namespaces | [Cohort 2 W9D1](https://www.youtube.com/watch?v=pTyaJQAN6tM) | Cohort 2 Rails API repositories |

## Next JavaScript and React mappings

| Lesson | Recording | Candidate source |
| --- | --- | --- |
| JavaScript fundamentals | [Cohort 2 W11D1](https://www.youtube.com/watch?v=sDzzZ2Hvdb0) | `modern-js` |
| JavaScript data | [Cohort 2 W11D2](https://www.youtube.com/watch?v=63HiSNt1dFw) | `modern-js` |
| Loops and iteration | [Cohort 2 W11D3](https://www.youtube.com/watch?v=jvupC1Yr5pw) | `modern-js` |
| React components and props | [Cohort 2 W13D2](https://www.youtube.com/watch?v=tUPxrIdwr_E) | Cohort 2 React repositories |
| Loading API data | [Cohort 2 W13D3](https://www.youtube.com/watch?v=3SW_W7PmEd4) | `full-stack-app` |
| Create actions | [Cohort 2 W14D1](https://www.youtube.com/watch?v=ONQWBuboH6A) | `full-stack-app` |
| Update and delete actions | [Cohort 2 W14D2](https://www.youtube.com/watch?v=jq7eXTuQRmc) | `full-stack-app` |
| Full-stack deployment | [Cohort 2 W15D5](https://www.youtube.com/watch?v=Otzinb2xcuQ) | `full-stack-app` |

## Next Python, FastAPI, and AI mappings

| Lesson | Recording | Candidate source |
| --- | --- | --- |
| Moving from JavaScript to Python | [Cohort 2 W16D1](https://www.youtube.com/watch?v=6L_8jqmVe8o) | Reconstruct only if no exact class repository is found |
| Python API development | [Cohort 2 W16D2](https://www.youtube.com/watch?v=qTh6G1_MyI8) | Reconstruct only if no exact class repository is found |
| Chatbots and API wrappers | [Cohort 2 W16D3](https://www.youtube.com/watch?v=fCXHKhI82Bw) | `spam-bots-chatbot` |

## Verification state

`Candidate source` is not a claim that the repository matches the recording. Before promoting an entry to `README.md`:

1. locate the commits immediately before and after the lesson change;
2. watch the recording and confirm the code, versions, and behavior;
3. verify both snapshots from a clean clone;
4. add focused timestamps, optional practice, and self-check criteria;
5. run the privacy check in `CONTRIBUTING.md`.

The Cohort 2 playlist contains 79 recordings, while the available local live/final archive contains 72. Keep that reconciliation open until every playlist item has either a matching local file or a documented hosted-only source.
