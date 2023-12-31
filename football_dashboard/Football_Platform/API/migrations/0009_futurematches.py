# Generated by Django 5.0 on 2023-12-21 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0008_view_scores_and_fixtures'),
    ]

    operations = [
        migrations.CreateModel(
            name='FutureMatches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='match_id', max_length=100, null=True)),
                ('match_date', models.DateField(blank=True, db_column='Match_Date', null=True)),
                ('home_team', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Home_Team', max_length=100, null=True)),
                ('home_manager', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Home_Manager', max_length=100, null=True)),
                ('home_captain', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Home_Captain', max_length=100, null=True)),
                ('home_formation', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Home_Formation', max_length=100, null=True)),
                ('home_possession', models.FloatField(blank=True, db_column='Home_Possession', null=True)),
                ('home_fouls', models.FloatField(blank=True, db_column='Home_Fouls', null=True)),
                ('home_corners', models.FloatField(blank=True, db_column='Home_Corners', null=True)),
                ('home_crosses', models.FloatField(blank=True, db_column='Home_Crosses', null=True)),
                ('home_aerials_won', models.FloatField(blank=True, db_column='Home_Aerials_Won', null=True)),
                ('home_clearances', models.FloatField(blank=True, db_column='Home_Clearances', null=True)),
                ('home_offsides', models.FloatField(blank=True, db_column='Home_Offsides', null=True)),
                ('home_goal_kicks', models.FloatField(blank=True, db_column='Home_Goal_Kicks', null=True)),
                ('home_throw_ins', models.FloatField(blank=True, db_column='Home_Throw_Ins', null=True)),
                ('home_long_balls', models.FloatField(blank=True, db_column='Home_Long_Balls', null=True)),
                ('home_total_players_stats', models.FloatField(blank=True, db_column='Home_Total_Players_Stats', null=True)),
                ('home_minutes', models.FloatField(blank=True, db_column='Home_Minutes', null=True)),
                ('home_gls', models.FloatField(blank=True, db_column='Home_Gls', null=True)),
                ('home_ast', models.FloatField(blank=True, db_column='Home_Ast', null=True)),
                ('home_pk', models.FloatField(blank=True, db_column='Home_PK', null=True)),
                ('home_pk_att', models.FloatField(blank=True, db_column='Home_PK_Att', null=True)),
                ('home_sh', models.FloatField(blank=True, db_column='Home_Sh', null=True)),
                ('home_sot', models.FloatField(blank=True, db_column='Home_SoT', null=True)),
                ('home_crdy', models.FloatField(blank=True, db_column='Home_CrdY', null=True)),
                ('home_crdr', models.FloatField(blank=True, db_column='Home_CrdR', null=True)),
                ('home_touches', models.FloatField(blank=True, db_column='Home_Touches', null=True)),
                ('home_tkl', models.FloatField(blank=True, db_column='Home_Tkl', null=True)),
                ('home_int', models.FloatField(blank=True, db_column='Home_Int', null=True)),
                ('home_blocks', models.FloatField(blank=True, db_column='Home_Blocks', null=True)),
                ('home_xg', models.FloatField(blank=True, db_column='Home_xG', null=True)),
                ('home_npxg', models.FloatField(blank=True, db_column='Home_npxG', null=True)),
                ('home_xag', models.FloatField(blank=True, db_column='Home_xAG', null=True)),
                ('home_sca', models.FloatField(blank=True, db_column='Home_SCA', null=True)),
                ('home_gca', models.FloatField(blank=True, db_column='Home_GCA', null=True)),
                ('home_cmp_passes', models.FloatField(blank=True, db_column='Home_Cmp_Passes', null=True)),
                ('home_att_passes', models.FloatField(blank=True, db_column='Home_Att_Passes', null=True)),
                ('home_cmp_percent_passes', models.FloatField(blank=True, db_column='Home_Cmp_percent_Passes', null=True)),
                ('home_prgp_passes', models.FloatField(blank=True, db_column='Home_PrgP_Passes', null=True)),
                ('home_carries_carries', models.FloatField(blank=True, db_column='Home_Carries_Carries', null=True)),
                ('home_prgc_carries', models.FloatField(blank=True, db_column='Home_PrgC_Carries', null=True)),
                ('home_att_take_ons', models.FloatField(blank=True, db_column='Home_Att_Take_Ons', null=True)),
                ('home_succ_take_ons', models.FloatField(blank=True, db_column='Home_Succ_Take_Ons', null=True)),
                ('away_team', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Away_Team', max_length=100, null=True)),
                ('away_manager', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Away_Manager', max_length=100, null=True)),
                ('away_captain', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Away_Captain', max_length=100, null=True)),
                ('away_formation', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Away_Formation', max_length=100, null=True)),
                ('away_possession', models.FloatField(blank=True, db_column='Away_Possession', null=True)),
                ('away_fouls', models.FloatField(blank=True, db_column='Away_Fouls', null=True)),
                ('away_corners', models.FloatField(blank=True, db_column='Away_Corners', null=True)),
                ('away_crosses', models.FloatField(blank=True, db_column='Away_Crosses', null=True)),
                ('away_aerials_won', models.FloatField(blank=True, db_column='Away_Aerials_Won', null=True)),
                ('away_clearances', models.FloatField(blank=True, db_column='Away_Clearances', null=True)),
                ('away_offsides', models.FloatField(blank=True, db_column='Away_Offsides', null=True)),
                ('away_goal_kicks', models.FloatField(blank=True, db_column='Away_Goal_Kicks', null=True)),
                ('away_throw_ins', models.FloatField(blank=True, db_column='Away_Throw_Ins', null=True)),
                ('away_long_balls', models.FloatField(blank=True, db_column='Away_Long_Balls', null=True)),
                ('away_total_players_stats', models.FloatField(blank=True, db_column='Away_Total_Players_Stats', null=True)),
                ('away_minutes', models.FloatField(blank=True, db_column='Away_Minutes', null=True)),
                ('away_gls', models.FloatField(blank=True, db_column='Away_Gls', null=True)),
                ('away_ast', models.FloatField(blank=True, db_column='Away_Ast', null=True)),
                ('away_pk', models.FloatField(blank=True, db_column='Away_PK', null=True)),
                ('away_pk_att', models.FloatField(blank=True, db_column='Away_PK_Att', null=True)),
                ('away_sh', models.FloatField(blank=True, db_column='Away_Sh', null=True)),
                ('away_sot', models.FloatField(blank=True, db_column='Away_SoT', null=True)),
                ('away_crdy', models.FloatField(blank=True, db_column='Away_CrdY', null=True)),
                ('away_crdr', models.FloatField(blank=True, db_column='Away_CrdR', null=True)),
                ('away_touches', models.FloatField(blank=True, db_column='Away_Touches', null=True)),
                ('away_tkl', models.FloatField(blank=True, db_column='Away_Tkl', null=True)),
                ('away_int', models.FloatField(blank=True, db_column='Away_Int', null=True)),
                ('away_blocks', models.FloatField(blank=True, db_column='Away_Blocks', null=True)),
                ('away_xg', models.FloatField(blank=True, db_column='Away_xG', null=True)),
                ('away_npxg', models.FloatField(blank=True, db_column='Away_npxG', null=True)),
                ('away_xag', models.FloatField(blank=True, db_column='Away_xAG', null=True)),
                ('away_sca', models.FloatField(blank=True, db_column='Away_SCA', null=True)),
                ('away_gca', models.FloatField(blank=True, db_column='Away_GCA', null=True)),
                ('away_cmp_passes', models.FloatField(blank=True, db_column='Away_Cmp_Passes', null=True)),
                ('away_att_passes', models.FloatField(blank=True, db_column='Away_Att_Passes', null=True)),
                ('away_cmp_percent_passes', models.FloatField(blank=True, db_column='Away_Cmp_percent_Passes', null=True)),
                ('away_prgp_passes', models.FloatField(blank=True, db_column='Away_PrgP_Passes', null=True)),
                ('away_carries_carries', models.FloatField(blank=True, db_column='Away_Carries_Carries', null=True)),
                ('away_prgc_carries', models.FloatField(blank=True, db_column='Away_PrgC_Carries', null=True)),
                ('away_att_take_ons', models.FloatField(blank=True, db_column='Away_Att_Take_Ons', null=True)),
                ('away_succ_take_ons', models.FloatField(blank=True, db_column='Away_Succ_Take_Ons', null=True)),
                ('home_attack', models.FloatField(blank=True, db_column='Home_Attack', null=True)),
                ('home_midfield', models.FloatField(blank=True, db_column='Home_Midfield', null=True)),
                ('home_defense', models.FloatField(blank=True, db_column='Home_Defense', null=True)),
                ('away_attack', models.FloatField(blank=True, db_column='Away_Attack', null=True)),
                ('away_midfield', models.FloatField(blank=True, db_column='Away_Midfield', null=True)),
                ('away_defense', models.FloatField(blank=True, db_column='Away_Defense', null=True)),
                ('home_score', models.FloatField(blank=True, db_column='Home_Score', null=True)),
                ('away_score', models.FloatField(blank=True, db_column='Away_Score', null=True)),
                ('result', models.CharField(blank=True, db_collation='utf8mb3_general_ci', db_column='Result', max_length=100, null=True)),
            ],
            options={
                'db_table': 'future_matches',
                'managed': False,
            },
        ),
    ]
