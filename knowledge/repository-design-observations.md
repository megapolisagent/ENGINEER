# Наблюдения о repository-design

> Не решения — подтверждённые внешней сверкой факты о текущем устройстве Skill, ожидающие решения владельца. Наличие наблюдения не означает, что Skill нужно менять — это отдельный, ещё не принятый шаг.

## 2026-08-12 — Внешняя сверка с практикой (Researcher)

Вопрос передан Researcher (`OPEN_QUESTIONS.md`, закрыт 2026-08-12): соответствует ли чек-лист `repository-design` реальной практике AI agent engineering, что он системно не замечает. Критерий ответа зафиксирован до поиска: конкретные пункты «подтверждено/отсутствует», каждый с источником.

**Подтверждено практикой** (чек-лист делает правильно):
- честно пустой `PROFILE.md`, не выдумывать факты о владельце — совпадает с `CAPABILITY_MAP.md` Capability 1;
- Skills только через `installer`, не вручную в тело агента — `CAPABILITY_MAP.md` Capability 8 («Fat engine, thin skill»);
- финальный пункт «проверено на реальной задаче» отделён от «чек-лист пройден» — независимо совпадает с паттерном Proof-or-Stop / Verify-Gated Completion, тем же классом, что и находка про Exit Gate.

**Observed gaps** (находка, не решение о переносе):

1. **Least-privilege / allowed-tools verification** — чек-лист ни разу не проверяет, соответствуют ли `allowed-tools` каждого Skill минимально необходимому набору (например, `installer` несёт `allowed-tools: Bash` — самый широкий из всех установленных Skills). Источники: `CAPABILITY_MAP.md` Capability 4 (deny > ask > allow); Microsoft Security Blog, «Least privilege for AI agents: Identity, access, and tool binding» (2026); OWASP AI Agent Security Cheat Sheet.
2. **Repeatable evaluation / regression trigger** — пункт 10 чек-листа однократный, без триггера «сверить заново, когда Skill или `HOME.md` изменились». Подтверждено собственным вторым прогоном аудита (`workspace/2026-08-12-repository-design-audit.md`) — расхождение `repository-design` со складом Skill System было бы не замечено без ручного повторного прогона. Источники: `CAPABILITY_MAP.md` Capability 10 (eval-gated promotion); MLflow, «Building Production-Ready AI Agents in 2026».
3. **Producer ≠ reviewer independence** — чек-лист требует «сверено с эталоном Researcher», но не требует структурной независимости проверяющего от проверяемого. Источник: `CAPABILITY_MAP.md` Capability 5 (fresh-reviewer instance, asymmetric persistence by role).

**Статус:** Observed, not adopted into `repository-design`.

**Решение владельца (2026-08-12):** не вносить сейчас. Researcher доказала наличие blind spots, но не доказала, что покрывать их должен именно `repository-design` — least-privilege может принадлежать отдельной security-проверке, reproducible eval — механизму Foundation, а не Skill, producer≠reviewer — routing/role-механизму. Присвоить находке носителя сейчас значило бы незаметно превратить исследовательский результат в архитектурное решение. `Proposal` не создан — статус зафиксирован в `DECISIONS.md`, запись 2026-08-12.

Источник: исследование Researcher, переданное 2026-08-12; `OPEN_QUESTIONS.md`, запись закрыта 2026-08-12.
