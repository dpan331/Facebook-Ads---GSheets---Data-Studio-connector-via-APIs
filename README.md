# Facebook-Ads---custom-Google-Data-Studio-connector
In this short guide I explain briefly the basic steps to build a custom Data Studio connector for Facebook Ads using the Marketing API and the Sheets API.

The main idea is simple and rather straightforward. Instead of building a community data connector we choose a workaround described in the steps below:
- First, we establish a connection with the Marketing API which gives us access to Facebook Ads data.
- Then, we establish a connection with Sheets API which gives us access to edit Google Sheets in our account.
- Finally, once we set up the data flow and see Facebook Ads data appear in our Google Sheets file, we use the official Google Sheets data connector to connect Google Data Studio with our Google Sheets file.


## Connect to the Marketing API

To do so we have to follow the relevant instructions: https://developers.facebook.com/docs/marketing-apis/get-started/

So all in all you need to 
1) Sign in to your FB developer account and create a new App. Then after you specify some general info about your App you should get your App's credentials, namely the **App ID** and **App Secret**
<img src="https://github.com/dpan331/Facebook_Ads---custom_Google_Data_Studio_connector/blob/main/img/app_developersAccount.JPG" height="300" width="1100">

2) Define the permissions you need (for fetching data **ads_read** permission should suffice) and get your Access Token. *Beware that depending on your choice the Access Token has a different expiration date. If you want your Access Token to last longer, you have to choose to proceed with the relevant option. In the current example we chose a short-term access token since the guide is only for educational purposes.*
<img src="https://github.com/dpan331/Facebook_Ads---custom_Google_Data_Studio_connector/blob/main/img/facebookGraphAPI_accessToken.JPG" height="300" width="800">

3) Go to your Facebook Ads UI (User Interface) and fetch the **Ad Account ID**.

4) In the current example we just fetch one Ad Set's spend to import to Google Sheets so we will need to fetch the Ad Set ID. If you build your own script though, you should go with whatever configuration you need. For example, you might simply need to fetch data on the campaign level. The specific configuration is up to you.

Finally in the python script that you can find in the current repository, use your own credentials wherever you see XXXXXXXXXXXXX (in the my_account variable keep the "act_" prefix in place, do not overwrite it).

Now if you run the script you should see in the output section the Ad Set spent for the date range you specified. In my case for the date range *'time_range': {'since':'2021-04-22','until':'2021-04-26'}* I get a spend of *2.51*. In order to be sure that the value I get is correct, I evaluate the output with a quick glance in my Facebook Ads UI>

<img src="https://github.com/dpan331/Facebook_Ads---custom_Google_Data_Studio_connector/blob/main/img/script_AdSetOutput.JPG" height="550" width="1100">

<img src="https://github.com/dpan331/Facebook_Ads---custom_Google_Data_Studio_connector/blob/main/img/FBAdsUI_adSet.JPG" height="200" width="1000">


## Connect to the Sheets API


