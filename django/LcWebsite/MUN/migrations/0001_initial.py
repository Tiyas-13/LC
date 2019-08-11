# Generated by Django 2.2.2 on 2019-08-09 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Committee1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(default='0123456789', max_length=15)),
                ('committee', models.CharField(choices=[('C1', 'United Nations General Assembly - DISEC'), ('C2', 'The All India Oppostion Meet')], default='C1', max_length=20)),
                ('college', models.CharField(default='NITD', max_length=200)),
                ('Past_Experience', models.CharField(default='None', max_length=1000)),
                ('preference1', models.CharField(choices=[('Prashant Kishore - Poll Strategist', 'Prashant Kishore - Poll Strategist'), ('Arvind Kejriwal-AAP', 'Arvind Kejriwal-AAP'), ('Manish Sisodia-AAP', 'Manish Sisodia-AAP'), ('Bhagwant Singh Mann-AAP', 'Bhagwant Singh Mann-AAP'), ('saduddin Owaisi- AIMIM', 'Asaduddin Owaisi- AIMIM'), ('Mamata Banerjee - AITMC', 'Mamata Banerjee - AITMC'), ('Derek OBrian - AITMC', 'Derek OBrian - AITMC'), ('Sudip Bandhopadhay - AITMC', 'Sudip Bandhopadhay - AITMC'), ('Mahua Moitra - AITMC', 'Mahua Moitra - AITMC'), ('Mayawati - BSP', 'Mayawati - BSP'), ('Satish Chandra Mishra - BSP', 'Satish Chandra Mishra - BSP'), ('Kunwar Danish Ali - BSP', 'Kunwar Danish Ali - BSP'), ('S. Sudhakar Reddy - CPI', 'S. Sudhakar Reddy - CPI'), ('K. Subbarayan - CPI', 'K. Subbarayan - CPI'), ('Sitaram Yechury - CPIM', 'Sitaram Yechury - CPIM'), ('anhaiya Kumar - CPIM', 'Kanhaiya Kumar - CPIM'), ('M K Stalin - DMK', 'M K Stalin - DMK'), ('T R Baalu - DMK', 'T R Baalu - DMK'), ('CTiruchi Siva - DMK', 'Tiruchi Siva - DMK'), ('Sonia Gandhi - INC', 'Sonia Gandhi - INC'), ('Rahul Gandhi - INC', 'Rahul Gandhi - INC'), ('Adhir Ranjan Chowdhury - INC', 'Adhir Ranjan Chowdhury - INC'), ('Shashi Tharoor - INC', 'Shashi Tharoor - INC'), ('Prianka Gandhi Vadra - INC', 'Prianka Gandhi Vadra - INC'), ('Ghulam Nabi Azad - INC', ' Ghulam Nabi Azad - INC'), ('Captain Araminder Singh - INC', 'Captain Araminder Singh - INC'), ('Kamal Nath - INC', 'Kamal Nath - INC'), ('C28', ''), ('Dr. Manmohan Singh - INC', 'Dr. Manmohan Singh - INC'), ('Siddharamia - INC', 'Siddharamia - INC'), ('Tarun Gogoi - INC', 'Tarun Gogoi - INC'), ('Ashok Ghelot - INC', 'Ashok Ghelot - INC'), ('P.Chidambaram - INC', 'P.Chidambaram - INC'), ('Randeep Surjewala - INC', 'Randeep Surjewala - INC'), ('Sheila Dixit - INC', 'Sheila Dixit - INC'), ('Hardik Patel - INC', 'Hardik Patel - INC'), ('KM Kader Mohideen - IUML', 'KM Kader Mohideen - IUML'), ('E T Mohammad Basheeer - IUML', 'E T Mohammad Basheeer - IUML'), ('H.D. Deve Gowda - JDS', 'H.D. Deve Gowda - JDS'), ('Shibhu Shoren - JMM', 'Shibhu Shoren - JMM'), ('Vijay Kumar Hansdak - JMM', 'Vijay Kumar Hansdak - JMM'), ('Omar Abdullah - J&KMC', 'Omar Abdullah - J&KMC'), ('Farooq Abdullah - J&KNC', 'Farooq Abdullah - J&KNC'), ('Mehbooba Mufti - J&K PDP', 'Mehbooba Mufti - J&K PDP'), ('Fayaz Ahmad Mir - J&K PDP', 'Fayaz Ahmad Mir - J&K PDP'), ('P S Joseph - Kerela Congress', 'P S Joseph - Kerela Congress'), ('R Balakrishna Pillai - Kerela Congress', 'R Balakrishna Pillai - Kerela Congress'), ('Raj Thackeray - MNS', 'Raj Thackeray - MNS'), ('Sharad Powar - NCP', 'Sharad Powar - NCP'), ('Supriya Sule - NCP', 'Supriya Sule - NCP'), ('Conrad Sangma - NPP', 'Conrad Sangma - NPP'), ('Agadha Sangma - NPP', 'Agadha Sangma - NPP'), ('Tejaswi Yadav - RJD', 'Tejaswi Yadav - RJD'), ('Ram Jethmalini - RJD', 'Ram Jethmalini - RJD'), ('T. J Chandrachoodan - RSP', 'T. J Chandrachoodan - RSP'), ('Akhilesh Yadav - SP', 'Akhilesh Yadav - SP'), ('Mulayam Singh Yadav - SP', 'Mulayam Singh Yadav - SP'), ('Azam Khan -SP', 'Azam Khan -SP'), ('Ram Gopal Yadav - SP', 'Ram Gopal Yadav - SP'), ('Jaydev Galla - TDP', 'Jaydev Galla - TDP'), ('Chandrababu Naidu - TDP', 'Chandrababu Naidu - TDP'), ('Afganistan', 'Afganistan'), ('Bangladesh', 'Bangladesh'), ('China', 'China'), ('Cambodia', 'Cambodia'), ('Bahrain', 'Bahrain'), ('India', 'India'), ('Iran', 'Iran'), ('Iraq', 'Iraq'), ('Israel', 'Israel'), ('Japan', 'Japan'), ('Jordan', 'Jordan'), ('Kuwait', 'Kuwait'), ('Lebanon', 'Lebanon'), ('Maldives', 'Maldives'), ('Macau', 'Macau'), ('Malasia', 'Malasia'), ('Mongolia', 'Mongolia'), ('Nepal', 'Nepal'), ('Pakistan', 'Pakistan'), ('Palestine', 'Palestine'), ('Russia', 'Russia'), ('Qatar', 'Qatar'), ('Saudi Arabia', 'Saudi Arabia'), ('Singapore', 'Singapore'), ('South Korea', 'South Korea'), ('Syria', 'Syria'), ('Taiwan', 'Taiwan'), ('Thailand', 'Thailand'), ('Turkey', 'Turkey'), ('UAE', 'UAE'), ('Vietnam', 'Vietnam'), ('Austria', 'Austria'), ('Belgium', 'Belgium'), ('Belarus', 'Belarus'), ('Bulgaria', 'Bulgaria'), ('Croatia', 'Croatia'), ('Denmark', 'Denmark'), ('Finland', 'Finland'), ('France', 'France'), ('Germany', 'Germany'), ('Greece', 'Greece'), ('Hungary', 'Hungary'), ('Ireland', 'Ireland'), ('Monaco', 'Monaco'), ('Norway', 'Norway'), ('Romania', 'Romania'), ('Serbia', 'Serbia'), ('Spain', 'Spain'), ('Sweden', 'Sweden'), ('Switzerland', 'Switzerland'), ('United Kingdom', 'United Kingdom'), ('Ukraine', 'Ukraine'), ('Algeria', 'Algeria'), ('Ethiopia', 'Ethiopia'), ('Ghana', 'Ghana'), ('Kenya', 'Kenya'), ('Libya', 'Libya'), ('Morocco', 'Morocco'), ('Mauritius', 'Mauritius'), ('Nigeria', 'Nigeria'), ('Somalia', 'Somalia'), ('Sudan', 'Sudan'), ('South Africa', 'South Africa'), ('Tanzania', 'Tanzania'), ('Uganda', 'Uganda'), ('Zimbabwe', 'Zimbabwe'), ('Barbados', 'Barbados'), ('Bermuds', 'Bermuds'), ('Canada', 'Canada'), ('Cuba', 'Cuba'), ('Costa Ric', 'Costa Rica'), ('Jamaica', 'Jamaica'), ('Mexico', 'Mexico'), ('Panama', 'Panama'), ('Puerto Rico', 'Puerto Rico'), ('United States of America', 'United States of America'), ('Argentina', 'Argentina'), ('Bolivia', 'Bolivia'), ('Brazil', 'Brazil'), ('Chile', 'Chile'), ('Columbia', 'Columbia'), ('Eucador', 'Eucador'), ('Paraguay', 'Paraguay'), ('Peru', 'Peru'), ('Uruguay', 'Uruguay'), ('Venezuela', 'Venezuela'), ('Australia', 'Australia'), ('New Zealand', 'New Zealand'), ('Fiji', 'Fiji')], default='None', max_length=300)),
                ('preference2', models.CharField(choices=[('Prashant Kishore - Poll Strategist', 'Prashant Kishore - Poll Strategist'), ('Arvind Kejriwal-AAP', 'Arvind Kejriwal-AAP'), ('Manish Sisodia-AAP', 'Manish Sisodia-AAP'), ('Bhagwant Singh Mann-AAP', 'Bhagwant Singh Mann-AAP'), ('saduddin Owaisi- AIMIM', 'Asaduddin Owaisi- AIMIM'), ('Mamata Banerjee - AITMC', 'Mamata Banerjee - AITMC'), ('Derek OBrian - AITMC', 'Derek OBrian - AITMC'), ('Sudip Bandhopadhay - AITMC', 'Sudip Bandhopadhay - AITMC'), ('Mahua Moitra - AITMC', 'Mahua Moitra - AITMC'), ('Mayawati - BSP', 'Mayawati - BSP'), ('Satish Chandra Mishra - BSP', 'Satish Chandra Mishra - BSP'), ('Kunwar Danish Ali - BSP', 'Kunwar Danish Ali - BSP'), ('S. Sudhakar Reddy - CPI', 'S. Sudhakar Reddy - CPI'), ('K. Subbarayan - CPI', 'K. Subbarayan - CPI'), ('Sitaram Yechury - CPIM', 'Sitaram Yechury - CPIM'), ('anhaiya Kumar - CPIM', 'Kanhaiya Kumar - CPIM'), ('M K Stalin - DMK', 'M K Stalin - DMK'), ('T R Baalu - DMK', 'T R Baalu - DMK'), ('CTiruchi Siva - DMK', 'Tiruchi Siva - DMK'), ('Sonia Gandhi - INC', 'Sonia Gandhi - INC'), ('Rahul Gandhi - INC', 'Rahul Gandhi - INC'), ('Adhir Ranjan Chowdhury - INC', 'Adhir Ranjan Chowdhury - INC'), ('Shashi Tharoor - INC', 'Shashi Tharoor - INC'), ('Prianka Gandhi Vadra - INC', 'Prianka Gandhi Vadra - INC'), ('Ghulam Nabi Azad - INC', ' Ghulam Nabi Azad - INC'), ('Captain Araminder Singh - INC', 'Captain Araminder Singh - INC'), ('Kamal Nath - INC', 'Kamal Nath - INC'), ('C28', ''), ('Dr. Manmohan Singh - INC', 'Dr. Manmohan Singh - INC'), ('Siddharamia - INC', 'Siddharamia - INC'), ('Tarun Gogoi - INC', 'Tarun Gogoi - INC'), ('Ashok Ghelot - INC', 'Ashok Ghelot - INC'), ('P.Chidambaram - INC', 'P.Chidambaram - INC'), ('Randeep Surjewala - INC', 'Randeep Surjewala - INC'), ('Sheila Dixit - INC', 'Sheila Dixit - INC'), ('Hardik Patel - INC', 'Hardik Patel - INC'), ('KM Kader Mohideen - IUML', 'KM Kader Mohideen - IUML'), ('E T Mohammad Basheeer - IUML', 'E T Mohammad Basheeer - IUML'), ('H.D. Deve Gowda - JDS', 'H.D. Deve Gowda - JDS'), ('Shibhu Shoren - JMM', 'Shibhu Shoren - JMM'), ('Vijay Kumar Hansdak - JMM', 'Vijay Kumar Hansdak - JMM'), ('Omar Abdullah - J&KMC', 'Omar Abdullah - J&KMC'), ('Farooq Abdullah - J&KNC', 'Farooq Abdullah - J&KNC'), ('Mehbooba Mufti - J&K PDP', 'Mehbooba Mufti - J&K PDP'), ('Fayaz Ahmad Mir - J&K PDP', 'Fayaz Ahmad Mir - J&K PDP'), ('P S Joseph - Kerela Congress', 'P S Joseph - Kerela Congress'), ('R Balakrishna Pillai - Kerela Congress', 'R Balakrishna Pillai - Kerela Congress'), ('Raj Thackeray - MNS', 'Raj Thackeray - MNS'), ('Sharad Powar - NCP', 'Sharad Powar - NCP'), ('Supriya Sule - NCP', 'Supriya Sule - NCP'), ('Conrad Sangma - NPP', 'Conrad Sangma - NPP'), ('Agadha Sangma - NPP', 'Agadha Sangma - NPP'), ('Tejaswi Yadav - RJD', 'Tejaswi Yadav - RJD'), ('Ram Jethmalini - RJD', 'Ram Jethmalini - RJD'), ('T. J Chandrachoodan - RSP', 'T. J Chandrachoodan - RSP'), ('Akhilesh Yadav - SP', 'Akhilesh Yadav - SP'), ('Mulayam Singh Yadav - SP', 'Mulayam Singh Yadav - SP'), ('Azam Khan -SP', 'Azam Khan -SP'), ('Ram Gopal Yadav - SP', 'Ram Gopal Yadav - SP'), ('Jaydev Galla - TDP', 'Jaydev Galla - TDP'), ('Chandrababu Naidu - TDP', 'Chandrababu Naidu - TDP'), ('Afganistan', 'Afganistan'), ('Bangladesh', 'Bangladesh'), ('China', 'China'), ('Cambodia', 'Cambodia'), ('Bahrain', 'Bahrain'), ('India', 'India'), ('Iran', 'Iran'), ('Iraq', 'Iraq'), ('Israel', 'Israel'), ('Japan', 'Japan'), ('Jordan', 'Jordan'), ('Kuwait', 'Kuwait'), ('Lebanon', 'Lebanon'), ('Maldives', 'Maldives'), ('Macau', 'Macau'), ('Malasia', 'Malasia'), ('Mongolia', 'Mongolia'), ('Nepal', 'Nepal'), ('Pakistan', 'Pakistan'), ('Palestine', 'Palestine'), ('Russia', 'Russia'), ('Qatar', 'Qatar'), ('Saudi Arabia', 'Saudi Arabia'), ('Singapore', 'Singapore'), ('South Korea', 'South Korea'), ('Syria', 'Syria'), ('Taiwan', 'Taiwan'), ('Thailand', 'Thailand'), ('Turkey', 'Turkey'), ('UAE', 'UAE'), ('Vietnam', 'Vietnam'), ('Austria', 'Austria'), ('Belgium', 'Belgium'), ('Belarus', 'Belarus'), ('Bulgaria', 'Bulgaria'), ('Croatia', 'Croatia'), ('Denmark', 'Denmark'), ('Finland', 'Finland'), ('France', 'France'), ('Germany', 'Germany'), ('Greece', 'Greece'), ('Hungary', 'Hungary'), ('Ireland', 'Ireland'), ('Monaco', 'Monaco'), ('Norway', 'Norway'), ('Romania', 'Romania'), ('Serbia', 'Serbia'), ('Spain', 'Spain'), ('Sweden', 'Sweden'), ('Switzerland', 'Switzerland'), ('United Kingdom', 'United Kingdom'), ('Ukraine', 'Ukraine'), ('Algeria', 'Algeria'), ('Ethiopia', 'Ethiopia'), ('Ghana', 'Ghana'), ('Kenya', 'Kenya'), ('Libya', 'Libya'), ('Morocco', 'Morocco'), ('Mauritius', 'Mauritius'), ('Nigeria', 'Nigeria'), ('Somalia', 'Somalia'), ('Sudan', 'Sudan'), ('South Africa', 'South Africa'), ('Tanzania', 'Tanzania'), ('Uganda', 'Uganda'), ('Zimbabwe', 'Zimbabwe'), ('Barbados', 'Barbados'), ('Bermuds', 'Bermuds'), ('Canada', 'Canada'), ('Cuba', 'Cuba'), ('Costa Ric', 'Costa Rica'), ('Jamaica', 'Jamaica'), ('Mexico', 'Mexico'), ('Panama', 'Panama'), ('Puerto Rico', 'Puerto Rico'), ('United States of America', 'United States of America'), ('Argentina', 'Argentina'), ('Bolivia', 'Bolivia'), ('Brazil', 'Brazil'), ('Chile', 'Chile'), ('Columbia', 'Columbia'), ('Eucador', 'Eucador'), ('Paraguay', 'Paraguay'), ('Peru', 'Peru'), ('Uruguay', 'Uruguay'), ('Venezuela', 'Venezuela'), ('Australia', 'Australia'), ('New Zealand', 'New Zealand'), ('Fiji', 'Fiji')], default='None', max_length=300)),
                ('preference3', models.CharField(choices=[('Prashant Kishore - Poll Strategist', 'Prashant Kishore - Poll Strategist'), ('Arvind Kejriwal-AAP', 'Arvind Kejriwal-AAP'), ('Manish Sisodia-AAP', 'Manish Sisodia-AAP'), ('Bhagwant Singh Mann-AAP', 'Bhagwant Singh Mann-AAP'), ('saduddin Owaisi- AIMIM', 'Asaduddin Owaisi- AIMIM'), ('Mamata Banerjee - AITMC', 'Mamata Banerjee - AITMC'), ('Derek OBrian - AITMC', 'Derek OBrian - AITMC'), ('Sudip Bandhopadhay - AITMC', 'Sudip Bandhopadhay - AITMC'), ('Mahua Moitra - AITMC', 'Mahua Moitra - AITMC'), ('Mayawati - BSP', 'Mayawati - BSP'), ('Satish Chandra Mishra - BSP', 'Satish Chandra Mishra - BSP'), ('Kunwar Danish Ali - BSP', 'Kunwar Danish Ali - BSP'), ('S. Sudhakar Reddy - CPI', 'S. Sudhakar Reddy - CPI'), ('K. Subbarayan - CPI', 'K. Subbarayan - CPI'), ('Sitaram Yechury - CPIM', 'Sitaram Yechury - CPIM'), ('anhaiya Kumar - CPIM', 'Kanhaiya Kumar - CPIM'), ('M K Stalin - DMK', 'M K Stalin - DMK'), ('T R Baalu - DMK', 'T R Baalu - DMK'), ('CTiruchi Siva - DMK', 'Tiruchi Siva - DMK'), ('Sonia Gandhi - INC', 'Sonia Gandhi - INC'), ('Rahul Gandhi - INC', 'Rahul Gandhi - INC'), ('Adhir Ranjan Chowdhury - INC', 'Adhir Ranjan Chowdhury - INC'), ('Shashi Tharoor - INC', 'Shashi Tharoor - INC'), ('Prianka Gandhi Vadra - INC', 'Prianka Gandhi Vadra - INC'), ('Ghulam Nabi Azad - INC', ' Ghulam Nabi Azad - INC'), ('Captain Araminder Singh - INC', 'Captain Araminder Singh - INC'), ('Kamal Nath - INC', 'Kamal Nath - INC'), ('C28', ''), ('Dr. Manmohan Singh - INC', 'Dr. Manmohan Singh - INC'), ('Siddharamia - INC', 'Siddharamia - INC'), ('Tarun Gogoi - INC', 'Tarun Gogoi - INC'), ('Ashok Ghelot - INC', 'Ashok Ghelot - INC'), ('P.Chidambaram - INC', 'P.Chidambaram - INC'), ('Randeep Surjewala - INC', 'Randeep Surjewala - INC'), ('Sheila Dixit - INC', 'Sheila Dixit - INC'), ('Hardik Patel - INC', 'Hardik Patel - INC'), ('KM Kader Mohideen - IUML', 'KM Kader Mohideen - IUML'), ('E T Mohammad Basheeer - IUML', 'E T Mohammad Basheeer - IUML'), ('H.D. Deve Gowda - JDS', 'H.D. Deve Gowda - JDS'), ('Shibhu Shoren - JMM', 'Shibhu Shoren - JMM'), ('Vijay Kumar Hansdak - JMM', 'Vijay Kumar Hansdak - JMM'), ('Omar Abdullah - J&KMC', 'Omar Abdullah - J&KMC'), ('Farooq Abdullah - J&KNC', 'Farooq Abdullah - J&KNC'), ('Mehbooba Mufti - J&K PDP', 'Mehbooba Mufti - J&K PDP'), ('Fayaz Ahmad Mir - J&K PDP', 'Fayaz Ahmad Mir - J&K PDP'), ('P S Joseph - Kerela Congress', 'P S Joseph - Kerela Congress'), ('R Balakrishna Pillai - Kerela Congress', 'R Balakrishna Pillai - Kerela Congress'), ('Raj Thackeray - MNS', 'Raj Thackeray - MNS'), ('Sharad Powar - NCP', 'Sharad Powar - NCP'), ('Supriya Sule - NCP', 'Supriya Sule - NCP'), ('Conrad Sangma - NPP', 'Conrad Sangma - NPP'), ('Agadha Sangma - NPP', 'Agadha Sangma - NPP'), ('Tejaswi Yadav - RJD', 'Tejaswi Yadav - RJD'), ('Ram Jethmalini - RJD', 'Ram Jethmalini - RJD'), ('T. J Chandrachoodan - RSP', 'T. J Chandrachoodan - RSP'), ('Akhilesh Yadav - SP', 'Akhilesh Yadav - SP'), ('Mulayam Singh Yadav - SP', 'Mulayam Singh Yadav - SP'), ('Azam Khan -SP', 'Azam Khan -SP'), ('Ram Gopal Yadav - SP', 'Ram Gopal Yadav - SP'), ('Jaydev Galla - TDP', 'Jaydev Galla - TDP'), ('Chandrababu Naidu - TDP', 'Chandrababu Naidu - TDP'), ('Afganistan', 'Afganistan'), ('Bangladesh', 'Bangladesh'), ('China', 'China'), ('Cambodia', 'Cambodia'), ('Bahrain', 'Bahrain'), ('India', 'India'), ('Iran', 'Iran'), ('Iraq', 'Iraq'), ('Israel', 'Israel'), ('Japan', 'Japan'), ('Jordan', 'Jordan'), ('Kuwait', 'Kuwait'), ('Lebanon', 'Lebanon'), ('Maldives', 'Maldives'), ('Macau', 'Macau'), ('Malasia', 'Malasia'), ('Mongolia', 'Mongolia'), ('Nepal', 'Nepal'), ('Pakistan', 'Pakistan'), ('Palestine', 'Palestine'), ('Russia', 'Russia'), ('Qatar', 'Qatar'), ('Saudi Arabia', 'Saudi Arabia'), ('Singapore', 'Singapore'), ('South Korea', 'South Korea'), ('Syria', 'Syria'), ('Taiwan', 'Taiwan'), ('Thailand', 'Thailand'), ('Turkey', 'Turkey'), ('UAE', 'UAE'), ('Vietnam', 'Vietnam'), ('Austria', 'Austria'), ('Belgium', 'Belgium'), ('Belarus', 'Belarus'), ('Bulgaria', 'Bulgaria'), ('Croatia', 'Croatia'), ('Denmark', 'Denmark'), ('Finland', 'Finland'), ('France', 'France'), ('Germany', 'Germany'), ('Greece', 'Greece'), ('Hungary', 'Hungary'), ('Ireland', 'Ireland'), ('Monaco', 'Monaco'), ('Norway', 'Norway'), ('Romania', 'Romania'), ('Serbia', 'Serbia'), ('Spain', 'Spain'), ('Sweden', 'Sweden'), ('Switzerland', 'Switzerland'), ('United Kingdom', 'United Kingdom'), ('Ukraine', 'Ukraine'), ('Algeria', 'Algeria'), ('Ethiopia', 'Ethiopia'), ('Ghana', 'Ghana'), ('Kenya', 'Kenya'), ('Libya', 'Libya'), ('Morocco', 'Morocco'), ('Mauritius', 'Mauritius'), ('Nigeria', 'Nigeria'), ('Somalia', 'Somalia'), ('Sudan', 'Sudan'), ('South Africa', 'South Africa'), ('Tanzania', 'Tanzania'), ('Uganda', 'Uganda'), ('Zimbabwe', 'Zimbabwe'), ('Barbados', 'Barbados'), ('Bermuds', 'Bermuds'), ('Canada', 'Canada'), ('Cuba', 'Cuba'), ('Costa Ric', 'Costa Rica'), ('Jamaica', 'Jamaica'), ('Mexico', 'Mexico'), ('Panama', 'Panama'), ('Puerto Rico', 'Puerto Rico'), ('United States of America', 'United States of America'), ('Argentina', 'Argentina'), ('Bolivia', 'Bolivia'), ('Brazil', 'Brazil'), ('Chile', 'Chile'), ('Columbia', 'Columbia'), ('Eucador', 'Eucador'), ('Paraguay', 'Paraguay'), ('Peru', 'Peru'), ('Uruguay', 'Uruguay'), ('Venezuela', 'Venezuela'), ('Australia', 'Australia'), ('New Zealand', 'New Zealand'), ('Fiji', 'Fiji')], default='None', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='IP1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(default='0123456789', max_length=15)),
                ('Choice', models.CharField(choices=[('IPJ', 'International Press Journalist'), ('IPP', 'International Press Photographer')], default='IPJ', max_length=20)),
                ('college', models.CharField(default='NITD', max_length=200)),
                ('Past_Experience', models.CharField(default='None', max_length=1000)),
                ('preference1', models.CharField(choices=[('The Hindu', 'The Hindu - All India Opposition'), ('The Telegraph', 'The Telegraph - All India Opposition'), ('The Pioneer', 'The Pioneer - All India Opposition'), ('Al Jazeera', 'Al Jazeera - Yemen Crisis'), ('BBC', 'BBC - Yemen Crisis'), ('Reuters', 'Reuters - Yemen Crisis')], default='Organisation', max_length=20)),
                ('preference2', models.CharField(choices=[('The Hindu', 'The Hindu - All India Opposition'), ('The Telegraph', 'The Telegraph - All India Opposition'), ('The Pioneer', 'The Pioneer - All India Opposition'), ('Al Jazeera', 'Al Jazeera - Yemen Crisis'), ('BBC', 'BBC - Yemen Crisis'), ('Reuters', 'Reuters - Yemen Crisis')], default='Organisation', max_length=20)),
                ('preference3', models.CharField(choices=[('The Hindu', 'The Hindu - All India Opposition'), ('The Telegraph', 'The Telegraph - All India Opposition'), ('The Pioneer', 'The Pioneer - All India Opposition'), ('Al Jazeera', 'Al Jazeera - Yemen Crisis'), ('BBC', 'BBC - Yemen Crisis'), ('Reuters', 'Reuters - Yemen Crisis')], default='Organisation', max_length=20)),
            ],
        ),
    ]
