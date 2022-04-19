# Facebook-Ads--GSheets--Data-Studio-connector-via-APIs
In this short guide I explain briefly the basic steps to build a custom Data Studio connector for Facebook Ads using the Marketing API and the Sheets API.

🚸 This script is not maintained, so, in time, certain operations or even the entire script may not be functional.

The main idea is simple and rather straightforward. Instead of building a community data connector we choose a workaround described in the steps below:
- First, we establish a connection with the Marketing API which gives us access to Facebook Ads data.
- Then, we establish a connection with Sheets API which gives us access to edit Google Sheets in our account.
- Finally, once we set up the data flow and see Facebook Ads data appear in our Google Sheets file, we use the official Google Sheets data connector to connect Google Data Studio with our Google Sheets file.


## Connect to the Marketing API

To do so we have to follow the relevant instructions: https://developers.facebook.com/docs/marketing-apis/get-started/

So all in all you need to 
1) Sign in to your FB developer account and create a new App. Then after you specify some general info about your App you should get your App's credentials, namely the **App ID** and **App Secret**
<img src="https://github.com/dpan331/Facebook_Ads---custom_Google_Data_Studio_connector/blob/main/img/app_developersAccount.jpg" height="300" width="1100">

2) Define the permissions you need (for fetching data **ads_read** permission should suffice) and get your Access Token. *Beware that depending on your choice the Access Token has a different expiration date. If you want your Access Token to last longer, you have to choose to proceed with the relevant option. In the current example we chose a short-term access token since the guide is only for educational purposes.*
<img src="https://github.com/dpan331/Facebook_Ads---custom_Google_Data_Studio_connector/blob/main/img/facebookGraphAPI_accessToken.jpg" height="300" width="800">

3) Go to your Facebook Ads UI (User Interface) and fetch the **Ad Account ID**.

4) In the current example we just fetch one Ad Set's spend to import to Google Sheets so we will need to fetch the Ad Set ID. If you build your own script though, you should go with whatever configuration you need. For example, you might simply need to fetch data on the campaign level. The specific configuration is up to you.

Finally in the python script that you can find in the current repository, use your own credentials wherever you see XXXXXXXXXXXXX (in the my_account variable keep the "act_" prefix in place, do not overwrite it).

Now if you run the script you should see in the output section the Ad Set spent for the date range you specified. In my case for the date range *'time_range': {'since':'2021-04-22','until':'2021-04-26'}* I get a spend of *2.51*. In order to be sure that the value I get is correct, I evaluate the output with a quick glance in my Facebook Ads UI>

<img src="https://github.com/dpan331/Facebook_Ads---custom_Google_Data_Studio_connector/blob/main/img/script_AdSetOutput.jpg" height="550" width="1100">

<img src="https://github.com/dpan331/Facebook_Ads---custom_Google_Data_Studio_connector/blob/main/img/FBAdsUI_adSet.JPG" height="200" width="1000">


## Connect to the Sheets API

To do so we have to follow the relevant instructions: https://developers.google.com/sheets/api/quickstart/python

1) Create a Google Cloud Platform project in https://console.cloud.google.com/
2) In your project enable the Google Sheets API.
3) Create authorization credentials for a desktop application.
4) Create your **credentials.json** and **token.json** files. *Make sure that these files are in the same folder that your python script exists*.
5) Pip install the relevant python library *--upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib*.
6) Create a sample Google Sheets file and get the **Spreadsheet ID** (you can find this number in the URL between the "d/" and "/edit" as shown in the screenshot below) and define the **cell range** you want to throw in data. *Make sure that you replace the XXXXXXXXX in the relevant fields of the python script".

So once I have all the set up and configuration in place, I run the script. I should see the spend fetched from the Facebook Ads' ad set (*2.51*) to appear in the A2 cell of Sheet2 of my Sample Spreadsheet.

<img src="https://github.com/dpan331/Facebook_Ads---custom_Google_Data_Studio_connector/blob/main/img/sampleSpreadsheet.JPG" height="600" width="1200">

## Connect your Google Data Studio report to the Google Sheets Spreadsheet

Open https://datastudio.google.com/

and create a Blank Report. 

The UI will prompt you to add a Data Source. Choose "Google Sheets" and specify your sample spreadsheet and relevant sheet. 

<img src="https://github.com/dpan331/Facebook_Ads---custom_Google_Data_Studio_connector/blob/main/img/connectionToGDS.JPG" height="600" width="1000">

You are done!
Now you can visualize your data from Facebook Ads however you want.

<img src="https://github.com/dpan331/Facebook_Ads---custom_Google_Data_Studio_connector/blob/main/img/GDSreport.JPG" height="400" width="1200">

## Some points for consideration

This guide is only an introduction to how to build a custom Google Data Studio connector for Facebook Ads using a workaround.
The Connector is not dynamic, meaning that the user cannot specify i.e. a date range in the Data Studio report and the data source to proceed in requesting those data from the Marketing API and show it in the visualization.

However, depending on how you need your report to be customized you can work on further workarounds.
A simple one being if for example you need a time series of a campaign's spend, you can schedule the python script to run daily, fetch yesterday's data and append it in a Google Sheets sheet with an additional column that will specify the date. This way you will be able to draft a time series plot in a Data Studio report AND add a date range control in order for the user to pick the historical date range she/he wants.

## Facebook-Ads--GSheets-connector-via-HTTP-Request

🤓 Also keep in mind that since Facebook's Graph API is based on HTTP Requests the most straightforward way to connect your Google Sheets spreadsheet to Graph API is by simply making a call to the respective url. 
Simply go to a cell and input ="https://graph.facebook.com/v11.0/act_YOUR-AD-ACCOUNT-ID/insights?date_preset=last_14d&level=campaign&action_report_time=conversion&fields=campaign_name,campaign_id,impressions,spend,conversions&access_token="&YOUR-ACCESS-TOKEN
(If you input the url above in your browser and hit enter, you will get your campaign's insights in json format).
To decouple the data from the json format to a tabular format you can use a custom Apps Script function like the one here https://github.com/bradjasper/ImportJSON.

Imagination, creativity and persistence is the key!


