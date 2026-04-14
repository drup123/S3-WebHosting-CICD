import json

def lambda_handler(event, context):
    name = event.get("name", "User")

    response = {
        "message": f"Hello {name} 🚀",
        "status": "success"
    }

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
