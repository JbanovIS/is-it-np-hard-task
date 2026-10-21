# Поиск по своей библиотеке: The nuclear fuel loading pattern optimization problem

[источник] OpenAlex, запрос: https://api.openalex.org/works?search=The+nuclear+fuel+loading+pattern+optimization+problem&per_page=50&filter=has_abstract%3Atrue&select=id%2Cdoi%2Cdisplay_name%2Cpublication_year%2Ccited_by_count%2Cabstract_inverted_index, дата: 2026-10-20, работ: 20

## доказательство NP-сложности задачи оптимизации загрузки ядерного топлива

| место | BM25 | вектор |
|---|---|---|
| 1 | Optimization of IRT-T Research Reactor Fuel Loading Pattern  (W7160177329) | Optimization of IRT-T Research Reactor Fuel Loading Pattern  (W7160177329) |
| 2 | — | Research on in-core fuel loading optimization of PWR nuclear (W2391072466) |
| 3 | — | Parallel Computing Fuel Assembly Loading Pattern Optimizatio (W203873291) |

[написано] Что подошло и чем выдачи отличаются: BM25 на русском запросе практически ничего не нашел (прочерки на 2 и 3 местах) из-за несовпадения языков; векторный поиск благодаря мультиязычным эмбеддингам подтянул релевантные работы по загрузке PWR (W2391072466).

## proof of NP-hardness for fuel loading pattern optimization problem

| место | BM25 | вектор |
|---|---|---|
| 1 | Optimization of IRT-T Research Reactor Fuel Loading Pattern  (W7160177329) | A loading patterns optimization method for nuclear fuel mana (W2516314432) |
| 2 | Fuel Loading Pattern Optimization with Constraint on Fuel As (W2810613334) | Fuel Loading Pattern Optimization with Constraint on Fuel As (W2810613334) |
| 3 | MYRRHA core loading pattern optimization using metaheuristic (W2521207856) | Loading pattern optimization for a PWR using Multi-Swarm Mot (W2996026804) |

[написано] Что подошло и чем выдачи отличаются: на английском запросе сработали обе модели, однако, ожидаемой разницы по типу "BM25 нашел статьи с точными терминами из запроса, а векторный поиск вывел более разнообразные ответы" не наблюдается. Оба алгоритма пытались ухватится за "fuel loading pattern optimization", видимо потому, что статей, где описывается NP-сложность этой задачи в их базе просто нет.

## NP-сложность задачи оптимизации загрузки ядерного топлива

| место | BM25 | вектор |
|---|---|---|
| 1 | Optimization of IRT-T Research Reactor Fuel Loading Pattern  (W7160177329) | Research on in-core fuel loading optimization of PWR nuclear (W2391072466) |
| 2 | — | Optimization of IRT-T Research Reactor Fuel Loading Pattern  (W7160177329) |
| 3 | — | A loading patterns optimization method for nuclear fuel mana (W2516314432) |

[написано] Что подошло и чем выдачи отличаются: BM25 не справился с русскоязычной формулировкой (2 и 3 места пусты), тогда как векторная модель успешно подобрала подходяще (по крайне мере по назанию) статьи.

## использование DRL алгоритмов для решения задачи оптимизации загрузки ядерного топлива

| место | BM25 | вектор |
|---|---|---|
| 1 | — | A loading patterns optimization method for nuclear fuel mana (W2516314432) |
| 2 | — | Optimization of IRT-T Research Reactor Fuel Loading Pattern  (W7160177329) |
| 3 | — | Multicycle Fuel Loading Pattern Optimization by Multiobjecti (W2071328844) |

[написано] Что подошло и чем выдачи отличаются: BM25 не справился с русскоязычной формулировкой совсем, тогда как векторная модель успешно подобрала подходящие статьи. Пару из этих статей я знаю, и в их названии нет "DRL", но они про применение DRL методов к инересующей меня задачи.

## использование квантовых метод для решения задачи оптимизации загрузки ядерного топлива

| место | BM25 | вектор |
|---|---|---|
| 1 | — | Quantum and quantum-inspired optimization for an in-core fue (W4392170357) |
| 2 | — | A loading patterns optimization method for nuclear fuel mana (W2516314432) |
| 3 | — | A Discrete Optimization Method for Nuclear Fuel Management (W3187982907) |

[написано] Что подошло и чем выдачи отличаются: BM25 не справился с русскоязычной формулировкой совсем, тогда как векторная модель успешно подобрала подходящие статьи.
