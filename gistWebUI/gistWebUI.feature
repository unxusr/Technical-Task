Feature: Gist WebUI test
        Scenario: Login, add new gist and comment
                Given i logged in successfully
                When i create a gist
                Then i should be able to edit the gist
                And i should be able to post a comments
                And i can delete a comment successfully

