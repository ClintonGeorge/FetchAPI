# My submission for the Backend Software Engineer Apprentice role @ Fetch Rewards

## The python framework, fastapi, was used to build this application.
## instrustions to run the code:

Open the terminal window and enter the following command that will retrieve the docker image from my docker hub repo and create and start the container:
```
docker run -p 8000:8000 cgeorge1/fetchapi:v6
```
This should start up the server and you should see an output similar to this.

<img width="631" alt="image" src="https://user-images.githubusercontent.com/32846700/217070583-deeaa13b-6b17-4b91-b62b-1166ebdb3a9b.png">

Paste this url in your browser or click on it [http://localhost:8000/docs](http://localhost:8000/docs) to navigate to the swagger UI where we can try out the API endpoints.

You should see a page similar to this.

<img width="1512" alt="image" src="https://user-images.githubusercontent.com/32846700/217075314-a9d61ea6-0490-4a96-aa9d-f71d25826356.png">

Let's try out the API!

Navigate to the Processor documentation and click on the Try Out button on the right side of the screen.

<img width="1512" alt="image" src="https://user-images.githubusercontent.com/32846700/217076226-d716b044-851f-440c-9036-9dfa393d960f.png">

Paste the following JSON request under Request Body.

```
{
  "retailer": "M&M Corner Market",
  "purchaseDate": "2022-03-20",
  "purchaseTime": "14:33",
  "items": [
    {
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    }
  ],
  "total": "9.00"
}
```
Scroll down a bit and you should see a similar output if the API call was successful.

<img width="1419" alt="image" src="https://user-images.githubusercontent.com/32846700/217077109-926fab91-afca-44ee-8aa4-e4f885e2ceb9.png">

Copy the id without the quotes. In my case the id was

![image](https://user-images.githubusercontent.com/32846700/217077744-440270e5-de7e-483e-9b17-05c3e5f4fa56.png)

Keep in mind that a new id is randomly generated after every successful call.

Navigate to the Points API endpoint and click the 'Try out' button on the right and paste the id you got from your previous call to the id section to the API and you receive a response similar to this.

<img width="1420" alt="Screenshot 2023-02-06 at 2 31 36 PM" src="https://user-images.githubusercontent.com/32846700/217079424-4833f60b-5301-4bf7-a6cd-f9ee72b2e5b6.png">

At the bottom of the page we can see that the receipt with the id we pasted has rewarded us with 109 points!



