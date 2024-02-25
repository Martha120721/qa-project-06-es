import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())

def post_new_client_kit(name):
    if name is not None:
        name_json = {
            "name": name
        }
    else:
        name_json = {}
    user_body = data.user_body.copy()
    user_response = post_new_user(user_body)
    auth_token = user_response.json()["authToken"]
    headers = data.headers.copy()
    headers["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=name_json,
                         headers=headers)

response = post_new_client_kit("kit de prueba")
print(response.status_code)
print(response.json())

