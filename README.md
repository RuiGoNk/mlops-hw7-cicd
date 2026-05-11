# mlops-hw7-cicd
Домашнее задание 7 - CI/CD для ML-сервиса
## CI/CD Pipeline

GitHub Actions успешно настроен:
- Автоматический запуск при push
- Установка зависимостей из requirements.txt
- Запуск ML пайплайна (обучение RandomForest на Iris)
- Сборка Docker-образа
- Тестирование контейнера

## Как воспроизвести

```bash
git clone https://github.com/RuiGoNk/mlops-hw7-cicd.git
cd mlops-hw7-cicd
docker build -t ml-service .
docker run ml-service
