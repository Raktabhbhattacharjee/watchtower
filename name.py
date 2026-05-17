from openai import OpenAI

from app.core.config import settings


client = OpenAI(
    api_key=settings.openai_api_key
)


def main():

    models = client.models.list()

    for model in models.data:
        print(model.id)


if __name__ == "__main__":
    main()