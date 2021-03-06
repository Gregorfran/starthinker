###########################################################################
#
#  Copyright 2017 Google Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
###########################################################################

Conversion_Dimensions_Schema = [
  { "name":"Conversion_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Activity", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Activity_Group", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Activity_Group_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Activity_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Activity_Date_Time", "type":"DATETIME", "mode":"NULLABLE" },
  { "name":"Browser_Platform", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Channel_Mix", "type":"STRING", "mode":"NULLABLE" },
  { "name":"City", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Click_Count", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Connection_Type", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Conversion_Referrer", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Conversion_Url", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Country", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Rich_Media_Custom_Event_Count", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Rich_Media_Custom_Event_Path_Summary", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Days_Since_Attributed_Interaction", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Days_Since_First_Interaction", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Designated_Market_Area_Dma", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Attribution_Type", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Configuration", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Hours_Since_Attributed_Interaction", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Hours_Since_First_Interaction", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Impression_Count", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Interaction_Count_Click_Tracker", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Interaction_Count_Mobile_Rich_Media", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Interaction_Count_Mobile_Static_Image", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Interaction_Count_Mobile_Video", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Interaction_Count_Natural_Search", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Interaction_Count_Paid_Search", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Interaction_Count_Rich_Media", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Interaction_Count_Static_Image", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Interaction_Count_Video", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Mobile_Carrier", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Num_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Operating_System", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Operating_System_Version", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Ord_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Path_Length", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Path_Type", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Platform_Type", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Recalculated_Attribution_Type", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Rich_Media_Standard_Event_Count", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Rich_Media_Standard_Event_Path_Summary", "type":"STRING", "mode":"NULLABLE" },
  { "name":"State_Region", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Tran_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"U_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Zip_Postal_Code", "type":"STRING", "mode":"NULLABLE" }
]
