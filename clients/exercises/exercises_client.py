from typing import TypedDict
from httpx import Response
from tools.api_client import ApiClient


class GetExercisesQueryDict(TypedDict):
    """Запрос на получение списка заданий курса."""
    courseId: str


class CreateExerciseRequestDict(TypedDict):
    """Запрос на создание задания."""
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex : int
    description : str
    estimatedTime: str


class UpdateExerciseRequestDict(TypedDict):
    """Запрос на обновление задания."""
    # TODO: посмотри в Swagger
    title: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str



class ExercisesClient(ApiClient):
    """API клиент для работы с заданиями (exercises)."""

    def update_exercise_api(self, exercise_id, request: UpdateExerciseRequestDict) -> Response:
        return self.patch(f'/api/v1/exercises/{exercise_id}', json=request)

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        return self.get('/api/v1/exercises', params=query)

    def post_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        return self.post('/api/v1/exercises', json=request)

    def get_exercise_api(self, exercise_id: str) -> Response:
        return self.get(f'/api/v1/exercises/{exercise_id}')

    def delete_exercise_api(self, exercise_id: str) -> Response:
        return self.delete(f'/api/v1/exercises/{exercise_id}')
