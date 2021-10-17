from drf_yasg import openapi

poll_answers = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "customer_id": openapi.Schema(type=openapi.TYPE_INTEGER, description="ID пользователя"),
        "poll": openapi.Schema(type=openapi.TYPE_INTEGER, description="ID опроса"),
        "answers": openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "question": openapi.Schema(type=openapi.TYPE_INTEGER, description="ID вопроса"),
                        "answer_text": openapi.Schema(type=openapi.TYPE_STRING, description="Текст ответа"),
                        "answer_choices": openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Schema(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    "id": openapi.Schema(type=openapi.TYPE_INTEGER, description="ID варианта ответа")
                                },
                                required=["id"]
                            ),
                            description="Варианты ответо"
                        )
                    },
                    required=["question"]
            ),
            description="list of questions with answers"
        ),
    },
    required=["customer_id", "poll"]
)
