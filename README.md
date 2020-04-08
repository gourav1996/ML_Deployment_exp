# ML_Deployment_exp
* Run the server code and request.py to check the sentiment 
* or save the inputdata in a .json file like:
{
    "x": ["I hate some movies"]
}

as test_data.json 
And run the curl command
* eg:  curl -XPOST http://localhost:8080/api -H 'Content-Type: application/json' -d @test_data.json
