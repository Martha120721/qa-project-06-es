import sender_stand_request
import data

def positive_assert(name):
    kit_response = sender_stand_request.post_new_client_kit(name)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name

def negative_assert_code_400(name):
    kit_response = sender_stand_request.post_new_client_kit(name)
    assert kit_response.status_code == 400


def test_name_1_character_response():
    positive_assert(data.one_letter)

def test_name_511_characters_response():
    positive_assert(data.multiple_characters_511)

def test_name_0_character_response():
    negative_assert_code_400(data.cero_character)

def test_name_512_characters_response():
    negative_assert_code_400(data.multiple_characters_512)

def test_name_special_characters_response():
    positive_assert(data.special_characters)

def test_name_space_1_response():
    positive_assert(data.one_space)

def test_name_numbers_response():
    positive_assert(data.multiple_numbers)

def test_name_0_parameter_response():
    negative_assert_code_400(data.none_value)

def test_name_special_parameter_response():
    negative_assert_code_400(data.special_value)