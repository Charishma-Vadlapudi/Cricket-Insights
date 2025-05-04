import pandas as pd
import json
import sys
with open("C:\\Users\\kalya\\Documents\\Charishma-Project\\Cricket Analysis-Top 11\\t20_json_files\\t20_wc_batting_summary.json","r") as f1:
    data1=json.load(f1)
records1=[]
for i in data1:
    records1.extend(i["battingSummary"])
t20_batting_summary_df=pd.DataFrame(records1)
t20_batting_summary_df['OUT']=t20_batting_summary_df['dismissal'].apply(lambda x:1 if len(x)>0 else 0)
with open("C:\\Users\\kalya\\Documents\\Charishma-Project\\Cricket Analysis-Top 11\\t20_json_files\\t20_wc_bowling_summary.json","r") as f2:
    data2=json.load(f2)
records2=[]
for i in data2:
    records2.extend(i['bowlingSummary'])
t20_bowling_summary_df=pd.DataFrame(records2)
with open("C:\\Users\\kalya\\Documents\\Charishma-Project\\Cricket Analysis-Top 11\\t20_json_files\\t20_wc_match_results.json","r") as f3:
    data3=json.load(f3)
records3=[]
for i in data3:
    records3.extend(i['matchSummary'])
t20_match_summary_df=pd.DataFrame(records3)
t20_match_summary_df.rename({'scorecard':'match_id'},axis=1,inplace=True)
match_id_dict={}
for index,row in t20_match_summary_df.iterrows():
  key1=row['team1']+' Vs '+row['team2']
  key2=row['team2']+' Vs '+row['team1']
  match_id_dict[key1]=row['match_id']
  match_id_dict[key2]=row['match_id']
t20_batting_summary_df['match']=t20_batting_summary_df['match'].map(match_id_dict)
t20_bowling_summary_df['match']=t20_bowling_summary_df['match'].map(match_id_dict)
with open("C:\\Users\\kalya\\Documents\\Charishma-Project\\Cricket Analysis-Top 11\\t20_json_files\\t20_wc_player_info.json","r") as f4:
    data4=json.load(f4)
t20_player_info_df=pd.DataFrame(data4)
t20_match_summary_df.to_csv("C:\\Users\\kalya\\Documents\\Charishma-Project\\Cricket Analysis-Top 11\\csv files\\t20_match_summary.csv",index=False)
t20_player_info_df.to_csv("C:\\Users\\kalya\\Documents\\Charishma-Project\\Cricket Analysis-Top 11\\csv files\\t20_player_info.csv",index=False)
t20_batting_summary_df.to_csv("C:\\Users\\kalya\\Documents\\Charishma-Project\\Cricket Analysis-Top 11\\csv files\\t20_batting_summary.csv",index=False)
t20_bowling_summary_df.to_csv("C:\\Users\\kalya\\Documents\\Charishma-Project\\Cricket Analysis-Top 11\\csv files\\t20_bowling_summary.csv",index=False)