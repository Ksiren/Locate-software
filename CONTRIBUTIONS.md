# Вклад участников

## M1 — lroofer

| Результат | Вклад | Проверяемый след |
| --- | --- | --- |
| Разделы 1, 2 и 4 паспорта | Назначение, граница продукта и сквозные сценарии | [PROJECT.md](PROJECT.md#1-назначение), [PR №2](https://github.com/Ksiren/Locate-software/pull/2) |
| Основа API и архитектура | Структура приложения, маршрут /health, тест и инструкция запуска | [README.md](README.md#архитектура), [HTTP-тест](tests/api/test_health.py), [PR №4](https://github.com/Ksiren/Locate-software/pull/4) |
| SR-ACCESS-01–03, T-ACCESS-01–03 и D-ACCESS-01 | Требования, угрозы и решение по доступу к заявкам и скрытым признакам; планы проверок | [Требования](SECURITY_REQUIREMENTS.md#sr-access-01), [угрозы](THREAT_MODEL.md#t-access-01), [решение](SECURITY_DECISIONS.md#d-access-01), [PR №5](https://github.com/Ksiren/Locate-software/pull/5) |

## M2

| Результат | Вклад | Проверяемый след |
| --- | --- | --- |
| Разделы 3, 5 и 7 паспорта | Роли, значимые данные и источники ввода | [Роли](PROJECT.md#3-пользователи-и-доступные-действия), [данные](PROJECT.md#5-значимые-данные-и-другие-объекты), [источники](PROJECT.md#7-откуда-продукт-получает-данные) |

## M3 — Irek-dev

| Результат | Вклад | Проверяемый след |
| --- | --- | --- |
| Разделы 6, 8 и 9 паспорта | Компоненты, минимальное ядро и стек | [Компоненты](PROJECT.md#6-компоненты-и-внешние-взаимодействия), [ядро](PROJECT.md#8-минимальное-функциональное-ядро), [стек](PROJECT.md#9-стек-и-путь-к-первой-работающей-версии), [PR №3](https://github.com/Ksiren/Locate-software/pull/3) |
| SR-ISS-01–03 и T-ISS-01–03 | Требования и угрозы по целостности выдачи, критерии приёмки | [Требования](SECURITY_REQUIREMENTS.md#sr-iss-01), [угрозы](THREAT_MODEL.md#t-iss-01), [PR №6](https://github.com/Ksiren/Locate-software/pull/6) |
| D-ISS-01 и CHECK-ISS-01–03 | Решение против неверной, повторной и частично сохранённой выдачи; планы проверок | [Решение](SECURITY_DECISIONS.md#d-iss-01), [проверки](SECURITY_DECISIONS.md#check-iss-01), [PR №6](https://github.com/Ksiren/Locate-software/pull/6) |

Механизмы доступа и выдачи ещё не реализованы; их предметные проверки описаны как план. Использование ИИ описано в [AI_USAGE.md](AI_USAGE.md).
