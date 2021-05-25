# Facebook-Ads---custom-Google-Data-Studio-connector
In this short guide I explain briefly the basic steps to build a custom Data Studio connector for Facebook Ads using the Marketing API and the Sheets API.

The main idea is simple and rather straightforward. Instead of building a community data connector we choose a workaround described in the steps below:
- First, we establish a connection with the Marketing API which gives us access to Facebook Ads data.
- Then, we establish a connection with Sheets API which gives us access to edit Google Sheets in our account.
- Finally, once we set up the data flow and see Facebook Ads data appear in our Google Sheets file, we use the official Google Sheets data connector to connect Google Data Studio with our Google Sheets file.

## Connect to the Marketing API

To do so we have to follow the relevant instructions: [https://developers.facebook.com/docs/marketing-apis/get-started/]

So all in all you need to 
1) Sign in to your FB developer account and create a new App. Then after you specify some general info about your App you should get your App's credentials, namely the **App ID** and **App Secret**
<img src="https://github.com/dpan331/Facebook_Ads---custom_Google_Data_Studio_connector/blob/main/img/app_developersAccount.JPG" height="300" width="1100">

2) define the permissions you need (for fetching data **ads_read** permission should suffice) and get your Access Token. *Beware that depending on your choice the Access Token has a different expiration date. If you want your Access Token to last longer, you have to choose to proceed with the relevant option. In the current example we chose a short-term access token since the guide is only for educational purposes.*
<img src="https://github.com/dpan331/Facebook_Ads---custom_Google_Data_Studio_connector/blob/main/img/facebookGraphAPI_accessToken.JPG" height="300" width="1100">


