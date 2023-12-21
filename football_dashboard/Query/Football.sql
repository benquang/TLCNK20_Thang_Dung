DROP database if exists Football;
CREATE DATABASE if not exists Football;
USE Football;
CREATE TABLE Matchs_Dataset_Model (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Match_Id NVARCHAR(100),
    Match_Date DATE,
    Home_Team NVARCHAR(100),
    Home_Manager NVARCHAR(100),
    Home_Captain NVARCHAR(100),
    Home_Formation NVARCHAR(100),
    Home_Possession FLOAT,
    Home_Fouls FLOAT,
    Home_Corners FLOAT,
    Home_Crosses FLOAT,
    Home_Aerials_Won FLOAT,
    Home_Clearances FLOAT,
    Home_Offsides FLOAT,
    Home_Goal_Kicks FLOAT,
    Home_Throw_Ins FLOAT,
    Home_Long_Balls FLOAT,
    Home_Total_Players_Stats FLOAT,
    Home_Minutes FLOAT,
    Home_Gls FLOAT,
    Home_Ast FLOAT,
    Home_PK FLOAT,
    Home_PK_Att FLOAT,
    Home_Sh FLOAT,
    Home_SoT FLOAT,
    Home_CrdY FLOAT,
    Home_CrdR FLOAT,
    Home_Touches FLOAT,
    Home_Tkl FLOAT,
    Home_Int FLOAT,
    Home_Blocks FLOAT,
    Home_xG FLOAT,
    Home_npxG FLOAT,
    Home_xAG FLOAT,
    Home_SCA FLOAT,
    Home_GCA FLOAT,
    Home_Cmp_Passes FLOAT,
    Home_Att_Passes FLOAT,
    Home_Cmp_percent_Passes FLOAT,
    Home_PrgP_Passes FLOAT,
    Home_Carries_Carries FLOAT,
    Home_PrgC_Carries FLOAT,
    Home_Att_Take_Ons FLOAT,
    Home_Succ_Take_Ons FLOAT,
    Away_Team NVARCHAR(100),
    Away_Manager NVARCHAR(100),
    Away_Captain NVARCHAR(100),
    Away_Formation NVARCHAR(100),
    Away_Possession FLOAT,
    Away_Fouls FLOAT,
    Away_Corners FLOAT,
    Away_Crosses FLOAT,
    Away_Aerials_Won FLOAT,
    Away_Clearances FLOAT,
    Away_Offsides FLOAT,
    Away_Goal_Kicks FLOAT,
    Away_Throw_Ins FLOAT,
    Away_Long_Balls FLOAT,
    Away_Total_Players_Stats FLOAT,
    Away_Minutes FLOAT,
    Away_Gls FLOAT,
    Away_Ast FLOAT,
    Away_PK FLOAT,
    Away_PK_Att FLOAT,
    Away_Sh FLOAT,
    Away_SoT FLOAT,
    Away_CrdY FLOAT,
    Away_CrdR FLOAT,
    Away_Touches FLOAT,
    Away_Tkl FLOAT,
    Away_Int FLOAT,
    Away_Blocks FLOAT,
    Away_xG FLOAT,
    Away_npxG FLOAT,
    Away_xAG FLOAT,
    Away_SCA FLOAT,
    Away_GCA FLOAT,
    Away_Cmp_Passes FLOAT,
    Away_Att_Passes FLOAT,
    Away_Cmp_percent_Passes FLOAT,
    Away_PrgP_Passes FLOAT,
    Away_Carries_Carries FLOAT,
    Away_PrgC_Carries FLOAT,
    Away_Att_Take_Ons FLOAT,
    Away_Succ_Take_Ons FLOAT,
    Home_Attack FLOAT,
    Home_Midfield FLOAT,
    Home_Defense FLOAT,
    Away_Attack FLOAT,
    Away_Midfield FLOAT,
    Away_Defense FLOAT,
    Home_Score FLOAT,
    Away_Score FLOAT
);

CREATE TABLE Fbref_Matchgoals_Modified (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Match_Id NVARCHAR(100),
    Team NVARCHAR(100),
    Minute FLOAT,
    Player_Name NVARCHAR(100),
    Type_Of_Goal NVARCHAR(100),
    Is_Home_Team NVARCHAR(100)
);

CREATE TABLE Fbref_Matchinfos_Modified (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Match_Id NVARCHAR(100),
    League NVARCHAR(100),
    Season NVARCHAR(100),
    Match_Week INT,
    Home_Team NVARCHAR(100),
    Away_Team NVARCHAR(100),
    Match_Date DATE,
    Venue_Time NVARCHAR(100),
    Attendance INT,
    Stadium NVARCHAR(100),
    Officials NVARCHAR(1000),
    Link NVARCHAR(200)
);

CREATE TABLE Fbref_Matchplayerstats_Modified (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Match_Id NVARCHAR(100),
    Team NVARCHAR(100),
    Player_Name NVARCHAR(100),
    Player_Kitnum INT,
    Nationality NVARCHAR(100),
    Position NVARCHAR(100),
    Age NVARCHAR(100),
    Minutes FLOAT,
    Gls FLOAT,
    Ast FLOAT,
    `PK` FLOAT,
    PK_Att FLOAT,
    Sh FLOAT,
    SoT FLOAT,
    CrdY FLOAT,
    CrdR FLOAT,
    Touches FLOAT,
    Tkl FLOAT,
    `Int` FLOAT,
    Blocks FLOAT,
    xG FLOAT,
    npxG FLOAT,
    xAG FLOAT,
    SCA FLOAT,
    GCA FLOAT,
    Passes_Cmp FLOAT,
    Passes_Att FLOAT,
    Passes_Cmp_Percentage FLOAT,
    Passes_PrgP FLOAT,
    Carries FLOAT,
    Carries_PrgC FLOAT,
    Take_Ons_Att FLOAT,
    Take_Ons_Succ FLOAT
);

CREATE TABLE Fbref_Matchsquad_Modified (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Match_Id NVARCHAR(100),
    Team NVARCHAR(100),
    Is_Home_Team nvarchar(100),
    Player_Name NVARCHAR(100),
    Player_Kitnum INT,
    Is_Sub NVARCHAR(100)
);
CREATE TABLE Fbref_Matchstats_Modified (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Match_Id NVARCHAR(100),
    Team NVARCHAR(100),
    Is_Home_Team nvarchar(100),
    Manager NVARCHAR(100),
    Captain NVARCHAR(100),
    Formation NVARCHAR(100),
    Possession FLOAT,
    Fouls FLOAT,
    Corners FLOAT,
    Crosses FLOAT,
    Aerials_Won FLOAT,
    Clearances FLOAT,
    Offsides FLOAT,
    Goal_Kicks FLOAT,
    Throw_Ins FLOAT,
    Long_Balls FLOAT,
    Total_Players_Stats FLOAT,
    Minutes FLOAT,
    Gls FLOAT,
    Ast FLOAT,
    PK FLOAT,
    PK_Att FLOAT,
    Sh FLOAT,
    SoT FLOAT,
    CrdY FLOAT,
    CrdR FLOAT,
    Touches FLOAT,
    Tkl FLOAT,
    `Int` FLOAT,
    Blocks FLOAT,
    xG FLOAT,
    npxG FLOAT,
    xAG FLOAT,
    SCA FLOAT,
    GCA FLOAT,
    Passes_Cmp FLOAT,
    Passes_Att FLOAT,
    Passes_Cmp_Percentage FLOAT,
    Passes_PrgP FLOAT,
    Carries FLOAT,
    Carries_PrgC FLOAT,
    Take_Ons_Att FLOAT,
    Take_Ons_Succ FLOAT,
    Score FLOAT
);
CREATE TABLE Matchsquad_Players (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Match_Id NVARCHAR(100),
    Match_Date DATE,
    Team NVARCHAR(100),
    Player_Name NVARCHAR(100),
    Player_Kitnum INT,
    Is_Sub NVARCHAR(100),
    Sofifa_Id NVARCHAR(100),
    Player_Position NVARCHAR(100),
    Player_Overall_Rating FLOAT,
    Player_Update_Date DATE
);
CREATE TABLE Sofifa_Players_Attr_Modified (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Acceleration FLOAT,
    Age INT,
    Aggression FLOAT,
    Agility FLOAT,
    All_Positions NVARCHAR(100),
    Attacking_Work_Rate NVARCHAR(100),
    Balance FLOAT,
    Ball_Control FLOAT,
    Birthday DATE,
    Body_Type NVARCHAR(100),
    Composure FLOAT,
    Crossing FLOAT,
    Curve FLOAT,
    Defensive_Awareness FLOAT,
    Defensive_Work_Rate NVARCHAR(100),
    Dribbling FLOAT,
    Finishing FLOAT,
    Fk_Accuracy FLOAT,
    Gk_Diving FLOAT,
    Gk_Handling FLOAT,
    Gk_Kicking FLOAT,
    Gk_Positioning FLOAT,
    Gk_Reflexes FLOAT,
    Heading_Accuracy FLOAT,
    Height NVARCHAR(100),
    Interceptions FLOAT,
    Jumping FLOAT,
    Long_Passing FLOAT,
    Long_Shots FLOAT,
    Marking FLOAT,
    Nationality NVARCHAR(100),
    Overall_Rating FLOAT,
    Penalties FLOAT,
    Player_Full_Name NVARCHAR(100),
    Player_Name NVARCHAR(100),
    Positioning FLOAT,
    Potential FLOAT,
    Preferred_Foot NVARCHAR(100),
    Reactions FLOAT,
    Real_Face NVARCHAR(100),
    Reputation FLOAT,
    Short_Passing FLOAT,
    Shot_Power FLOAT,
    Skill_Moves FLOAT,
    Sliding_Tackle FLOAT,
    Sofifa_Id nvarchar(100),
    Specialities NVARCHAR(100),
    Sprint_Speed FLOAT,
    Stamina FLOAT,
    Standing_Tackle FLOAT,
    Strength FLOAT,
    Team1 NVARCHAR(100),
    Team1_Contract INT,
    Team1_Joined DATE,
    Team1_Kitnum INT,
    Team1_Loaned_From NVARCHAR(100),
    Team1_Position NVARCHAR(100),
    Team1_Rating FLOAT,
    Team2 NVARCHAR(100),
    Team2_Kitnum INT,
    Team2_Position NVARCHAR(100),
    Team2_Rating FLOAT,
    Traits NVARCHAR(100),
    Update_Date DATE,
    Value NVARCHAR(100),
    Vision FLOAT,
    Volleys FLOAT,
    Wage NVARCHAR(100),
    Weak_Foot FLOAT,
    Weight FLOAT
);

CREATE TABLE Sofifa_Players_Infos_Modified (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Player_Id NVARCHAR(100),
    Birthday DATE,
    Player_Full_Name NVARCHAR(100),
    Player_Name NVARCHAR(100),
    Team_Club NVARCHAR(100),
    Nationality NVARCHAR(100),
    Height FLOAT,
    Weight FLOAT
);

CREATE TABLE future_matches (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Match_Id NVARCHAR(100),
    Match_Date DATE,
    Home_Team NVARCHAR(100),
    Home_Manager NVARCHAR(100),
    Home_Captain NVARCHAR(100),
    Home_Formation NVARCHAR(100),
    Home_Possession FLOAT,
    Home_Fouls FLOAT,
    Home_Corners FLOAT,
    Home_Crosses FLOAT,
    Home_Aerials_Won FLOAT,
    Home_Clearances FLOAT,
    Home_Offsides FLOAT,
    Home_Goal_Kicks FLOAT,
    Home_Throw_Ins FLOAT,
    Home_Long_Balls FLOAT,
    Home_Total_Players_Stats FLOAT,
    Home_Minutes FLOAT,
    Home_Gls FLOAT,
    Home_Ast FLOAT,
    Home_PK FLOAT,
    Home_PK_Att FLOAT,
    Home_Sh FLOAT,
    Home_SoT FLOAT,
    Home_CrdY FLOAT,
    Home_CrdR FLOAT,
    Home_Touches FLOAT,
    Home_Tkl FLOAT,
    Home_Int FLOAT,
    Home_Blocks FLOAT,
    Home_xG FLOAT,
    Home_npxG FLOAT,
    Home_xAG FLOAT,
    Home_SCA FLOAT,
    Home_GCA FLOAT,
    Home_Cmp_Passes FLOAT,
    Home_Att_Passes FLOAT,
    Home_Cmp_percent_Passes FLOAT,
    Home_PrgP_Passes FLOAT,
    Home_Carries_Carries FLOAT,
    Home_PrgC_Carries FLOAT,
    Home_Att_Take_Ons FLOAT,
    Home_Succ_Take_Ons FLOAT,
    Away_Team NVARCHAR(100),
    Away_Manager NVARCHAR(100),
    Away_Captain NVARCHAR(100),
    Away_Formation NVARCHAR(100),
    Away_Possession FLOAT,
    Away_Fouls FLOAT,
    Away_Corners FLOAT,
    Away_Crosses FLOAT,
    Away_Aerials_Won FLOAT,
    Away_Clearances FLOAT,
    Away_Offsides FLOAT,
    Away_Goal_Kicks FLOAT,
    Away_Throw_Ins FLOAT,
    Away_Long_Balls FLOAT,
    Away_Total_Players_Stats FLOAT,
    Away_Minutes FLOAT,
    Away_Gls FLOAT,
    Away_Ast FLOAT,
    Away_PK FLOAT,
    Away_PK_Att FLOAT,
    Away_Sh FLOAT,
    Away_SoT FLOAT,
    Away_CrdY FLOAT,
    Away_CrdR FLOAT,
    Away_Touches FLOAT,
    Away_Tkl FLOAT,
    Away_Int FLOAT,
    Away_Blocks FLOAT,
    Away_xG FLOAT,
    Away_npxG FLOAT,
    Away_xAG FLOAT,
    Away_SCA FLOAT,
    Away_GCA FLOAT,
    Away_Cmp_Passes FLOAT,
    Away_Att_Passes FLOAT,
    Away_Cmp_percent_Passes FLOAT,
    Away_PrgP_Passes FLOAT,
    Away_Carries_Carries FLOAT,
    Away_PrgC_Carries FLOAT,
    Away_Att_Take_Ons FLOAT,
    Away_Succ_Take_Ons FLOAT,
    Home_Attack FLOAT,
    Home_Midfield FLOAT,
    Home_Defense FLOAT,
    Away_Attack FLOAT,
    Away_Midfield FLOAT,
    Away_Defense FLOAT,
    Home_Score FLOAT,
    Away_Score FLOAT,
    Result NVARCHAR(100)
);

create view view_Scores_and_Fixtures as
select ROW_NUMBER() OVER (ORDER BY table1.Match_Id) AS id,
        table1.Match_Id,
		table1.League,
		table1.Season, 
		table1.Match_Week, 
		table1.Home_Team, 
		table1.Away_Team, 
		table1.Match_Date, 
		table1.Venue_Time, 
		table1.Attendance, 
		table1.Stadium, 
		table1.Officials, 
		table1.Link,
		table1.Score as Home_Score,
        table2.Score as Away_Score 
from (select matchinfos.*,matchstats.Score
		from fbref_matchinfos_modified matchinfos
		join fbref_matchstats_modified matchstats on matchinfos.Match_Id = matchstats.Match_Id 
		where matchstats.Is_Home_Team ="Yes") table1 
join (select matchinfos.*,matchstats.Score
		from fbref_matchinfos_modified matchinfos
		join fbref_matchstats_modified matchstats on matchinfos.Match_Id = matchstats.Match_Id 
		where matchstats.Is_Home_Team ="No") table2 on table1.Match_Id = table2.Match_Idview_scores_and_fixtures
        
