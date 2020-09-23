import unittest
import json
import requests
import os
from faker import Faker

fake = Faker()

class TestGistRequests(unittest.TestCase):
    
    global username,token,base_url,old_gist_id
    username = os.environ.get("username")
    token = os.environ.get("token")
    base_url = os.environ.get("baseUrl")
    old_gist_id = "19c6092c845cddb519fb625ba7c1d514"
    
    
    def setUp(self):
        print("Running", self._testMethodName)


    def test_create_gist(self):
        route = base_url + "/gists"
        headers = {"Accept": "application/vnd.github.v3+json"}
        payload = {"public":True,"files":{fake.word()+".txt":{"content":fake.sentence()}}}
        payload = json.dumps(payload)
        response = requests.post(route, headers=headers, data=payload, auth=(username, token))
        global new_gist_id
        new_gist_id = response.json()['id']
        assert response.status_code == 201

    def test_get_all_gists(self):
        route = base_url + "/gists"
        headers = {"Accept": "application/vnd.github.v3+json"}
        response = requests.get(route, headers=headers, auth=(username, token))
        assert response.status_code == 200
    
    def test_get_public_gist(self):
        route = base_url + "/gists/public"
        headers = {"Accept": "application/vnd.github.v3+json"}
        response = requests.get(route, headers=headers, auth=(username, token))
        assert response.status_code == 200
        assert response.json()[0]['public'] == True

    def test_get_gist(self):
        route = base_url + f"/gists/{old_gist_id}"
        headers = {"Accept": "application/vnd.github.v3+json"}
        response = requests.get(route, headers=headers, auth=(username, token))
        assert response.status_code == 200

    def test_list_starred_gists(self):
        route = base_url + f"/gists/starred"
        headers = {"Accept": "application/vnd.github.v3+json"}
        response = requests.get(route, headers=headers, auth=(username, token))
        assert response.status_code == 200

    def test_update_gist(self):
        route = base_url + f"/gists/{old_gist_id}"
        fake_description = fake.sentence()
        payload = {"description":fake_description}
        payload = json.dumps(payload)
        headers = {"Accept": "application/vnd.github.v3+json"}
        response = requests.patch(route, headers=headers, data=payload, auth=(username, token))
        assert response.status_code == 200
        assert response.json()['description'] == fake_description
    
    def test_list_gist_commits(self):
        route = base_url + f"/gists/{old_gist_id}/commits"
        headers = {"Accept": "application/vnd.github.v3+json"}
        response = requests.get(route, headers=headers, auth=(username, token))
        assert response.status_code == 200 

    def test_zdelete_gist(self):
        route = base_url + f"/gists/{new_gist_id}"
        headers = {"Accept": "application/vnd.github.v3+json"}
        response = requests.delete(route, headers=headers, auth=(username, token))
        assert response.status_code == 204

    def test_list_gist_forks(self):
        route = base_url + f"/gists/{old_gist_id}/commits"
        headers = {"Accept": "application/vnd.github.v3+json"}
        response = requests.get(route, headers=headers, auth=(username, token))
        assert response.status_code == 200

    def test_fork_gist(self):
        
        # The below request will fail due to this gist is forked before
        # It is not allowed to fork owned gists
        # Every gist is allowed to be forked for 1 time per account
        # Please insert a new gist ID in the below request and uncomment before running 
        pass # -> to be removed for actual running
        """
        route = base_url + "/gists/1207c168877af83e2b5a8b2142c93a90/forks"
        headers = {"Accept": "application/vnd.github.v3+json"}
        response = requests.post(route, headers=headers, auth=(username, token))
        print(response.json())
        assert response.status_code == 201
        """
        
    def test_check_if_gist_starred(self):
        
        # based on gist documentation this request has 2 success modes
        # 1st if the gist starred then request will finish with status 204 No Content
        # 2nd if the gist is not starred request will finish with status 404 Not Found

        username = os.environ.get("username")
        token = os.environ.get("token")
        base_url = os.environ.get("baseUrl")
        route = base_url + f"/gists/{old_gist_id}/star"
        headers = {"Accept": "application/vnd.github.v3+json"}
        response = requests.get(route, headers=headers, auth=(username, token))
        if response.status_code == 204:
            print("gist is starred")
            assert response.status_code == 204
        else:
            print("gist is not starred")
            assert response.status_code == 404
    
    def test_star_gist(self):
        route = base_url + f"/gists/{old_gist_id}/star"
        headers = {"Accept": "application/vnd.github.v3+json"}
        response = requests.put(route, headers=headers, auth=(username, token))
        assert response.status_code == 204
    
    def test_unstar_gist(self):
        route = base_url + f"/gists/{old_gist_id}/star"
        headers = {"Accept": "application/vnd.github.v3+json"}
        response = requests.delete(route, headers=headers, auth=(username, token))
        assert response.status_code == 204
    
    def test_get_gist_revision(self):
        route = base_url + "/gists/69eeb503125035f21a9d"
        headers = {"Accept": "application/vnd.github.v3+json"}
        response = requests.get(route, headers=headers, auth=(username, token))
        assert response.status_code == 200

    def test_list_user_gists(self):
        route = base_url + "/users/tott/gists"
        headers = {"Accept": "application/vnd.github.v3+json"}
        response = requests.get(route, headers=headers, auth=(username, token))
        assert response.status_code == 200

    def test_list_gist_comments(self):
        route = base_url + f"/gists/{old_gist_id}/comments"
        headers = {"Accept": "application/vnd.github.v3+json"}
        response = requests.get(route, headers=headers, auth=(username, token))
        assert response.status_code == 200

    def test_create_gist_comment(self):
        route = base_url + f"/gists/{old_gist_id}/comments"
        payload = {"body":fake.sentence()}
        payload = json.dumps(payload)
        headers = {"Accept": "application/vnd.github.v3+json"}
        response = requests.post(route, headers=headers, data=payload, auth=(username, token))
        global comment_id 
        comment_id = response.json()['id']
        assert response.status_code == 201

    def test_get_gist_comment(self):
        route = base_url + f"/gists/{old_gist_id}/comments/{comment_id}"
        headers = {"Accept": "application/vnd.github.v3+json"}
        response = requests.get(route, headers=headers, auth=(username, token))
        assert response.status_code == 200

    def test_update_gist_comment(self):
        route = base_url + f"/gists/{old_gist_id}/comments/{comment_id}"
        payload = {"body":fake.sentence()}
        payload = json.dumps(payload)
        headers = {"Accept": "application/vnd.github.v3+json"}
        response = requests.patch(route, headers=headers, data=payload, auth=(username, token))
        assert response.status_code == 200

    def test_zdelete_comment(self):
        route = base_url + f"/gists/{old_gist_id}/comments/{comment_id}"
        headers = {"Accept": "application/vnd.github.v3+json"}
        response = requests.delete(route, headers=headers, auth=(username, token))
        assert response.status_code == 204


    
if __name__ == '__main__':
    unittest.main()

