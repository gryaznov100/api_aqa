import pytest

TEST_DATA = [{'title': 'foo', 'body': 'bar', 'userId': 1}]
NEGATIVE_TEST_DATA = [{'title': ['foo---'], 'body': 'bar---', 'userId': 2}]


@pytest.mark.parametrize('payload', TEST_DATA)
def test_post_a_post(create_post_endpoint, payload):
    create_post_endpoint.create_new_post(payload)
    create_post_endpoint.assert_status_201()
    create_post_endpoint.assert_id(payload['userId'])


@pytest.mark.parametrize('payload', NEGATIVE_TEST_DATA)
def test_post_with_negative_data(create_post_endpoint, payload):
    create_post_endpoint.create_new_post(payload)
    create_post_endpoint.assert_title(payload['title'])


def test_put_a_post(update_post_endpoint):
    payload = {
        'title': 'foo---',
        'body': 'bar---',
        'userId': 2
    }
    update_post_endpoint.make_changes_in_post(42, payload)
    update_post_endpoint.assert_title(payload['title'])
    # assert response['title'] == 'foo---'
