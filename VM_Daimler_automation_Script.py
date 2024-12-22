import os
import datetime
import pandas as pd
import win32com.client as win32
import re
# import base64

server_owners = {
'S, Seetharaman': ['D365AID1AX300.in365.tbintra.net', 's365ald1vish124.in365.lia.corpintra.net', 's365ald1vish154.in365.lia.corpintra.net', 's365m009.apac.corpdir.net'],
'Ss, Manojkumar': ['d365aid1bcd198.in365.corpintra.net', 'd365aid1jbo225.in365.corpintra.net', 'd365aid1jbo226.in365.corpintra.net', 'd365aid1jbo227.in365.corpintra.net', 'd365aid1ltr228.in365.corpintra.net', 'd365aid1mfw221.in365.corpintra.net', 'd365aid1sos222.in365.corpintra.net', 'd365aid1vmat151.in365.corpintra.net', 'd365aid1vmmi145.in365.corpintra.net', 'd365aid1vmmi146.in365.corpintra.net', 'd365ald1vibm140.in365.lia.corpintra.net', 'd365bid1me188.in365.corpintra.net', 'D365BID1ME194.in365.tbintra.net', 'D365BID1ODS173.in365.tbintra.net', 'D365BID1PDS172.in365.tbintra.net', 'd365bid1vmat132.in365.corpintra.net', 'd365bld1vibm127.in365.lia.corpintra.net', 'd365ild1vibm065.in365.lia.corpintra.net', 's365aid1bcd207.in365.corpintra.net', 's365aid1ck305.in365.corpintra.net', 's365aid1ckd220.in365.corpintra.net', 's365aid1ckd310.in365.corpintra.net', 's365aid1ckd311.in365.corpintra.net', 's365aid1ep284.in365.corpintra.net', 's365aid1hp282.in365.corpintra.net', 's365aid1m035.in365.corpintra.net', 's365aid1m037.in365.corpintra.net', 's365aid1m039.in365.corpintra.net', 's365aid1m048.in365.corpintra.net', 's365aid1m050.in365.corpintra.net', 's365aid1m054.in365.corpintra.net', 's365aid1m069.in365.corpintra.net', 's365aid1m072.in365.corpintra.net', 's365aid1me231.in365.corpintra.net', 's365aid1me232.in365.corpintra.net', 's365aid1me233.in365.corpintra.net', 's365aid1me234.in365.corpintra.net', 's365aid1me235.in365.corpintra.net', 's365aid1me236.in365.corpintra.net', 's365aid1me237.in365.corpintra.net', 's365aid1me238.in365.corpintra.net', 's365aid1me239.in365.corpintra.net', 's365aid1me240.in365.corpintra.net', 's365aid1me241.in365.corpintra.net', 's365aid1me242.in365.corpintra.net', 's365aid1me243.in365.corpintra.net', 's365aid1me244.in365.corpintra.net', 's365aid1me245.in365.corpintra.net', 's365aid1me246.in365.corpintra.net', 's365aid1me247.in365.corpintra.net', 's365aid1me248.in365.corpintra.net', 's365aid1me249.in365.corpintra.net', 's365aid1me250.in365.corpintra.net', 's365aid1me251.in365.corpintra.net', 's365aid1me252.in365.corpintra.net', 's365aid1me264.in365.corpintra.net', 's365aid1me269.in365.corpintra.net', 's365aid1me270.in365.corpintra.net', 's365aid1me271.in365.corpintra.net', 's365aid1me272.in365.corpintra.net', 's365aid1me273.in365.corpintra.net', 's365aid1me274.in365.corpintra.net', 's365aid1me275.in365.corpintra.net', 's365aid1meg201.in365.corpintra.net', 'S365AID1MEG202.in365.corpintra.net', 's365aid1mp283.in365.corpintra.net', 's365aid1pp287.in365.corpintra.net', 's365aid1tp285.in365.corpintra.net', 's365aid1vmpm157.in365.corpintra.net', 's365aid1vp286.in365.corpintra.net', 's365ald1ib259.in365.lia.corpintra.net', 's365bid1bcd62.in365.corpintra.net', 's365bid1ck208.in365.corpintra.net', 's365bid1ckd171.in365.corpintra.net', 's365bid1m030.in365.corpintra.net', 's365bid1me176.in365.tbintra.net', 's365bid1me177.in365.tbintra.net', 's365bid1me178.in365.corpintra.net', 's365bid1me195.in365.corpintra.net', 's365bid1me196.in365.corpintra.net', 's365bid1me197.in365.corpintra.net', 's365bid1me198.in365.corpintra.net', 's365bid1me199.in365.corpintra.net', 's365bid1me200.in365.corpintra.net', 's365bid1me201.in365.corpintra.net', 's365bid1me202.in365.corpintra.net', 's365bid1me203.in365.corpintra.net', 's365bid1vmpm134.in365.corpintra.net', 's365bid1voms135.in365.corpintra.net', 's365bld1ib184.in365.lia.corpintra.net', 's365iid1me083.in365.corpintra.net', 's365ild1ib082.in365.lia.corpintra.net', 's365m152.in365.corpintra.net'],
'M, Rajeshwaran': ['d365aid1bms211.in365.corpintra.net'],
'Marimuthu, Mathusuthanan': ['d365aid1fvat139.in365.corpintra.net', 'd365aid1gt331.in365.corpintra.net', 'd365aid1si327.in365.corpintra.net', 'd365ald1fg096.in365.lia.corpintra.net', 'd365ald1vfsl126.in365.lia.corpintra.net', 'd365bid1gt220.in365.corpintra.net', 'd365bid1si216.in365.corpintra.net', 'd365bid1vfsl120.in365.corpintra.net', 'd365bidbvg3t141.in365.corpintra.net', 'd365bld1fg101.in365.lia.corpintra.net', 'd365bld1vfsl118.in365.lia.corpintra.net', 'd365ild1fg045.in365.lia.corpintra.net', 'd365ild1vfsl060.in365.lia.corpintra.net', 'd365mid1f042.in365.corpintra.net', 'd365mid1f043.in365.corpintra.net', 'q365aid1vfsl136.in365.corpintra.net', 's365aid1f027.in365.corpintra.net', 's365aid1f073.in365.corpintra.net', 's365aid1gt279.in365.corpintra.net', 's365aid1gt330.in365.corpintra.net', 's365aid1si329.in365.corpintra.net', 's365aid1vfke147.in365.corpintra.net', 's365aid1vfke148.in365.corpintra.net', 's365ald1fg095.in365.lia.corpintra.net', 's365ald1vfsl123.in365.lia.corpintra.net', 's365bid1gt205.in365.corpintra.net', 's365bid1gt219.in365.corpintra.net', 's365bid1si217.in365.corpintra.net', 's365bid1si218.in365.corpintra.net', 's365bid1vfsl116.in365.corpintra.net', 'S365BID1VFSL117.in365.tbintra.net', 's365bidbvg3t165.in365.corpintra.net', 's365bld1vfsl115.in365.lia.corpintra.net', 's365c011.in365.corpintra.net', 's365c012.in365.corpintra.net', 's365dld1fg068.in365.lia.corpintra.net', 's365ild1fg040.in365.lia.corpintra.net', 's365ild1vfsl059.in365.lia.corpintra.net', 's365m064.in365.corpintra.net', 's365m068.in365.corpintra.net', 'S365M142.in365.corpintra.net'],
'Jeevan, Gopikrishnan': ['d365aid1gr258.in365.corpintra.net', 'd365aid1gr267.in365.corpintra.net', 'D365AID1LD180.in365.corpintra.net', 'D365AID1PD181.in365.corpintra.net', 'D365AID1PQ190.in365.corpintra.net', 'D365AID1SD290.in365.corpintra.net', 'D365AID1SJ182.in365.corpintra.net', 'D365AID1VH149.in365.corpintra.net', 'D365AIDBOD165.in365.corpintra.net', 'D365AIDBWD164.in365.corpintra.net', 'd365ald1bq205.in365.lia.corpintra.net', 'd365ald1vg160.in365.lia.corpintra.net', 'd365bid1gr193.in365.corpintra.net', 'D365BID1VH150.in365.corpintra.net', 'D365BIDBLD142.in365.corpintra.net', 'D365BIDBOD139.in365.corpintra.net', 'D365BIDBPD143.in365.corpintra.net', 'D365BIDBPQ152.in365.corpintra.net', 'D365BIDBSM144.in365.corpintra.net', 'D365BIDBWD138.in365.corpintra.net', 'D365BLDBCS155.in365.corpintra.net', 'D365IDVBOBI71.in365.corpintra.net', 'd365ild1rp074.in365.lia.corpintra.net', 'd365ild1wds70.in365.lia.corpintra.net', 'D365MDID1CC03.in365.corpintra.net', 'i365dticidrvp07.in365.corpintra.net', 'i365dticidrvp08.in365.corpintra.net', 'S365AID1BO192.in365.corpintra.net', 'S365AID1BO193.in365.corpintra.net', 'S365AID1BO194.in365.corpintra.net', 's365aid1bo333.in365.tbintra.net', 'S365AID1BW170.in365.corpintra.net', 'S365AID1BW174.in365.corpintra.net', 'S365AID1BW175.in365.corpintra.net', 'S365AID1BW188.in365.corpintra.net', 'S365AID1DM171.in365.corpintra.net', 'S365AID1DM175.in365.corpintra.net', 'S365AID1DM176.in365.corpintra.net', 'S365AID1DM177.in365.corpintra.net', 'S365AID1DM178.in365.corpintra.net', 'S365AID1DM189.in365.corpintra.net', 'S365AID1DM199.in365.corpintra.net', 'S365AID1DM200.in365.corpintra.net', 's365aid1gr265.in365.corpintra.net', 's365aid1gr266.in365.corpintra.net', 's365aid1gr276.in365.corpintra.net', 'S365AID1LP172.in365.corpintra.net', 'S365AID1LP176.in365.corpintra.net', 'S365AID1LP177.in365.corpintra.net', 'S365AID1LP178.in365.corpintra.net', 'S365AID1LP179.in365.corpintra.net', 'S365AID1LQ191.in365.corpintra.net', 'S365AID1PP173.in365.corpintra.net', 'S365AID1PP177.in365.corpintra.net', 'S365AID1PP178.in365.corpintra.net', 's365aid1pr297.in365.corpintra.net', 's365aid1pr298.in365.corpintra.net', 'S365AID1SD289.in365.corpintra.net', 'S365AID1SJ185.in365.corpintra.net', 'S365AID1SM186.in365.corpintra.net', 's365ald1bp206.in365.lia.corpintra.net', 's365ald1dm276.in365.lia.corpintra.net', 's365ald1dp204.in365.lia.corpintra.net', 's365ald1wd168.in365.lia.corpintra.net', 'S365BID1BO160.in365.corpintra.net', 'S365BID1BW150.in365.corpintra.net', 'S365BID1DM151.in365.corpintra.net', 's365bid1gr191.in365.corpintra.net', 'S365BIDBBO159.in365.corpintra.net', 'S365BIDBBW145.in365.corpintra.net', 'S365BIDBDM147.in365.corpintra.net', 'S365BIDBLP148.in365.corpintra.net', 'S365BIDBLQ153.in365.corpintra.net', 'S365BIDBPP149.in365.corpintra.net', 'S365BIDBSM146.in365.corpintra.net', 'S365BLDBCS154.in365.corpintra.net', 'S365IID1BO072.in365.corpintra.net', 'S365IID1BO078.in365.corpintra.net', 's365ild1bp077.in365.lia.corpintra.net', 's365ild1dm076.in365.lia.corpintra.net', 's365ild1dm084.in365.lia.corpintra.net', 's365ild1rp075.in365.lia.corpintra.net', 's365mid1s024.in365.corpintra.net'],
'Mohana Sundaram, P': ['d365aid1lci212.in365.corpintra.net', 'd365aid1r083.in365.corpintra.net', 'D365BID1DT174.in365.tbintra.net', 'd365bid1r060.in365.corpintra.net', 's365aid1dl255.in365.corpintra.net', 's365aid1fp257.in365.corpintra.net', 's365aid1q031.in365.corpintra.net', 's365aid1r082.in365.corpintra.net', 's365ald1vccc108.in365.lia.corpintra.net', 's365bid1c066.in365.corpintra.net', 's365bid1dl180.in365.corpintra.net', 'S365BID1FP182.in365.tbintra.net', 's365bid1q070.in365.corpintra.net', 's365bid1r059.in365.corpintra.net', 's365bld1ckd168.in365.lia.corpintra.net', 's365id1qd043.in365.corpintra.net', 's365ild1vccc057.in365.lia.corpintra.net', 's365m177.in365.corpintra.net', 'S365MID1S016.in365.corpintra.net'],
'Raja, Ravi Kumar': ['d365aid1le281.in365.tbintra.net', 'd365aid1xw280.in365.corpintra.net', 'd365bid1xw206.in365.tbintra.net', 'd365bld1ds190.in365.lia.corpintra.net', 'q365ald1vep134.in365.lia.corpintra.net', 'q365bld1vep123.in365.lia.corpintra.net', 'q365ild1vep063.in365.lia.corpintra.net', 'S365AID1GDOT104.in365.tbintra.net', 's365aid1hr278.in365.tbintra.net', 's365aid1hr309.in365.corpintra.net', 's365aid1i056.in365.corpintra.net', 's365aid1ms261.in365.corpintra.net', 's365aid1pe314.in365.tbintra.net', 's365aid1qm313.in365.tbintra.net', 's365aid1sc260.in365.corpintra.net', 's365aid1vjen142.in365.corpintra.net', 's365aid1vjen143.in365.corpintra.net', 's365aid1vrpa161.in365.corpintra.net', 's365aid1vrpa162.in365.corpintra.net', 'S365AID1XW230.in365.tbintra.net', 's365ald1dep095.in365.lia.corpintra.net', 's365ald1sa256.in365.lia.corpintra.net', 's365ald1vsgc152.in365.lia.corpintra.net', 's365ald1vtlm141.in365.lia.corpintra.net', 's365ald1w018.in365.lia.corpintra.net', 's365bid1hr204.in365.tbintra.net', 's365bid1hr211.in365.corpintra.net', 's365bid1i019.in365.corpintra.net', 's365bid1ms186.in365.corpintra.net', 's365bid1pe214.in365.tbintra.net', 's365bid1q058.in365.corpintra.net', 's365bid1qm213.in365.tbintra.net', 's365bid1sc185.in365.corpintra.net', 's365bid4a005.in365.corpintra.net', 's365bid4a032.in365.corpintra.net', 's365bid4a033.in365.corpintra.net', 's365bid4vfa124.in365.corpintra.net', 's365bld1dep103.in365.lia.corpintra.net', 's365bld1ds189.in365.lia.corpintra.net', 'S365BLD1GDOT109.in365.tbintra.net', 's365bld1sa181.in365.lia.corpintra.net', 's365bld1sc179.in365.lia.corpintra.net', 's365bld1vsgc133.in365.lia.corpintra.net', 's365bld1vtlm128.in365.lia.corpintra.net', 's365bld1w011.in365.lia.corpintra.net', 's365id1i013.in365.corpintra.net', 's365id1qdg044.in365.corpintra.net', 's365id1qf042.in365.corpintra.net', 's365iid1hr086.in365.corpintra.net', 's365iid1pf088.in365.tbintra.net', 's365iid1qm087.in365.tbintra.net', 's365ild1dep048.in365.lia.corpintra.net', 's365ild1sa081.in365.lia.corpintra.net', 's365ild1vsgc068.in365.lia.corpintra.net', 's365ild1vtlm066.in365.lia.corpintra.net', 's365ild1w010.in365.lia.corpintra.net', 's365mid1v048.in365.corpintra.net', 's365mid4a027.in365.corpintra.net'],
'Jacob, Joy': ['d365aid1m092.in365.corpintra.net', 'd365aid1vs288.in365.corpintra.net', 'd365bid1m067.in365.corpintra.net', 'd365ild1dm093.in365.lia.corpintra.net', 's365ad1ob094.in365.corpintra.net', 's365aid1d001.in365.corpintra.net', 's365aid1d002.in365.corpintra.net', 's365aid1d003.in365.corpintra.net', 's365aid1d004.in365.corpintra.net', 's365aid1d005.in365.corpintra.net', 's365aid1d014.in365.corpintra.net', 's365aid1d017.in365.corpintra.net', 's365aid1d020.in365.corpintra.net', 'S365AID1DM315.in365.corpintra.net', 'S365AID1DM316.in365.corpintra.net', 'S365AID1DM317.in365.corpintra.net', 's365ald1d001.in365.lia.corpintra.net', 's365ald1d002.in365.lia.corpintra.net', 's365ald1d003.in365.lia.corpintra.net', 's365ald1d004.in365.lia.corpintra.net', 's365ald1d057.in365.lia.corpintra.net', 's365ald1s028.in365.lia.corpintra.net', 's365ald1s059.in365.lia.corpintra.net', 's365ald1vdob144.in365.lia.corpintra.net', 's365bd1ob095.in365.corpintra.net', 's365bid1d008.in365.corpintra.net', 's365bid1d013.in365.corpintra.net', 's365bld1d035.in365.lia.corpintra.net', 's365cid1d001.in365.corpintra.net', 's365cid1d002.in365.corpintra.net', 's365cid1d003.in365.corpintra.net', 's365cid1d004.in365.corpintra.net', 's365cld1d003.in365.lia.corpintra.net', 's365cld1d004.in365.lia.corpintra.net', 's365iid1d001.in365.corpintra.net', 'S365IID1D002.in365.corpintra.net', 's365iid1d003.in365.corpintra.net', 's365ild1d001.in365.lia.corpintra.net', 's365ild1d002.in365.lia.corpintra.net', 's365ild1d018.in365.lia.corpintra.net', 's365ild1dm092.in365.lia.corpintra.net', 's365ild1dm094.in365.lia.corpintra.net', 's365ild1vobi067.in365.lia.corpintra.net', 's365mid1d009.in365.corpintra.net'],
'Vairavan, Vinoth': ['d365aid1rm326.in365.corpintra.net', 's365m028.in365.tbintra.net', 's365mid1mo62.in365.corpintra.net'],
'K, Vikram': ['D365AID1TE195.in365.tbintra.net', 'd365ald1te214.in365.lia.corpintra.net', 'd365bid1te161.in365.corpintra.net', 'd365bld1te170.in365.lia.corpintra.net', 'd365ild1te079.in365.lia.corpintra.net', 'S365AID1TE210.in365.tbintra.net', 's365bid1te166.in365.corpintra.net'],
# '2023-09-01 06:53:03_NIRMALP (local)': ['d365aid1vdsc158.in365.corpintra.net', 'd365ald1vdis159.in365.lia.corpintra.net', 'd365bld1vdis136.in365.lia.corpintra.net', 'd365ild1vdis069.in365.lia.corpintra.net', 's365ald1sc254.in365.lia.corpintra.net', 's365ild1sc080.in365.lia.corpintra.net'],
# 'nan': ['d365aid1vmrm153.in365.corpintra.net', 'D365BID1VFSL119.in365.tbintra.net', 'd365mld1visn046.in365.lia.corpintra.net', 'q365mld1visn047.in365.lia.corpintra.net', 's365a001.in365.corpintra.net', 's365agpvem00.in365.corpintra.net', 's365aid1gt339.in365.tbintra.net', 's365aid1o089.in365.corpintra.net', 's365aid1rpsm106.apac.corpdir.net', 's365bid1ci221.in365.tbintra.net', 's365bid1ck212.in365.corpintra.net', 's365bid1ef224.in365.tbintra.net', 's365bid1gt226.in365.tbintra.net', 's365bid1p034.in365.corpintra.net', 's365bid1tf225.in365.tbintra.net', 's365bid1vh222.in365.tbintra.net', 's365bid1vm223.in365.tbintra.net', 'S365CHCI1000', 'S365CHCI1001', 'S365D0001001', 'S365D0001002', 'S365ILD1RP095.in365.lia.corpintra.net', 's365ild1rp096.in365.lia.corpintra.net', 's365ild1rp098.in365.lia.corpintra.net', 's365m011.in365.tbintra.net', 's365m028New.in365.tbintra.net', 's365mid1b037.in365.corpintra.net', 's365mid1o042.in365.corpintra.net', 's365mid1t049.in365.corpintra.net', 's365tld1j002.in365.lia.corpintra.net'],
'S, Siva': ['d365ald1vlmi133.in365.lia.corpintra.net', 'd365ild1vlmi062.in365.lia.corpintra.net'],
'Sankar, K': ['d365bd1wa102.in365.corpintra.net', 'd365mid1k038.in365.corpintra.net', 'q365bid1vfsl126.in365.corpintra.net', 's365a004.in365.corpintra.net', 's365aid1o090.in365.corpintra.net', 's365bd1wa100.in365.corpintra.net', 's365bid1a069.in365.corpintra.net', 's365bid1k076.in365.corpintra.net', 's365bid1n074.in365.corpintra.net', 's365bid1vrpa137.in365.corpintra.net', 's365bld1vfke131.in365.corpintra.net', 's365c016.in365.corpintra.net', 's365c023.in365.corpintra.net', 's365mid1d025.in365.corpintra.net', 's365mld1o044.in365.lia.corpintra.net', 's365mld1sc054.in365.lia.corpintra.net', 's365mld1sc055.in365.lia.corpintra.net'],
'M, Manjunatha': ['d365id1vwa047.in365.corpintra.net', 's365aid1ba324.in365.corpintra.net', 's365aid1c023.in365.corpintra.net', 's365ald1a010.in365.lia.corpintra.net', 's365bid1ba215.in365.corpintra.net', 's365bld1a007.in365.lia.corpintra.net', 's365bld1as210.in365.lia.corpintra.net', 's365ild1a009.in365.lia.corpintra.net', 's365m115.in365.corpintra.net'],
'Mohan, Sunantha': ['d365mid1l040.in365.corpintra.net', 'S365AID1A013.in365.corpintra.net', 'S365AID1P086.in365.corpintra.net', 'S365AID1P091.in365.corpintra.net', 's365aid1rchs128.in365.corpintra.net', 's365aid1u006.in365.corpintra.net', 's365bid1rchs122.in365.corpintra.net', 's365bid1u002.in365.corpintra.net', 'S365C025.in365.corpintra.net', 'S365C026.in365.corpintra.net', 'S365C027.in365.corpintra.net', 'S365C028.in365.corpintra.net', 's365cgpsma00-n1.in365.corpintra.net', 'S365M149.in365.corpintra.net', 'S365M150.in365.corpintra.net', 's365mid1l008.in365.corpintra.net', 's365mid1l019.in365.corpintra.net', 's365mid1l026.in365.corpintra.net', 's365mid1l038.in365.corpintra.net'],
'Kumar, Hemanth': ['I365KLD1VPX003.in365.corpintra.net', 'I365KLD1VPX004.in365.corpintra.net', 's365aid1a063.in365.corpintra.net', 's365aid1ax299.in365.corpintra.net', 'S365AID1AX301.in365.corpintra.net', 's365aid1qn328.in365.corpintra.net', 's365mid3b030.in365.corpintra.net'],
#'2023-03-18 05:50:26_SNADARA (local)': ['S365AD1PSCL116.in365.tbintra.net', 'S365AD1PSEC110.in365.corpintra.net', 'S365AD1PSEC111.in365.tbintra.net', 'S365AD1PSEC112.in365.tbintra.net', 'S365AD1PSKI119.in365.tbintra.net', 'S365AD1PSLO117.in365.tbintra.net', 'S365AD1PSSR121.in365.tbintra.net', 'S365AD1VSANC113.in365.corpintra.net', 'S365AD1VSANC114.in365.corpintra.net', 'S365AD1VSANC115.in365.corpintra.net', 'S365AD1VSON122.in365.corpintra.net'],
'P, Aravind': ['s365aid1a060.in365.corpintra.net'],
'V, Jaivinoth': ['s365aid1a077.in365.corpintra.net', 's365bid1a050.in365.corpintra.net', 's365iid1a029.in365.corpintra.net'],
'Kanagasabai, Saravanan': ['s365aid1das223.in365.corpintra.net', 's365ald1vssa132.in365.lia.corpintra.net', 's365ild1vssa061.in365.lia.corpintra.net', 'S365AD1PSCL116.in365.tbintra.net', 'S365AD1PSEC110.in365.corpintra.net', 'S365AD1PSEC111.in365.tbintra.net', 'S365AD1PSEC112.in365.tbintra.net', 'S365AD1PSKI119.in365.tbintra.net', 'S365AD1PSLO117.in365.tbintra.net', 'S365AD1PSSR121.in365.tbintra.net', 'S365AD1VSANC113.in365.corpintra.net', 'S365AD1VSANC114.in365.corpintra.net', 'S365AD1VSANC115.in365.corpintra.net', 'S365AD1VSON122.in365.corpintra.net'],
'Sridharan, S': ['s365aid1ip291.in365.corpintra.net', 's365aid1ip292.in365.corpintra.net', 's365bid1on187.in365.corintra.net', 's365p004.in365.corpintra.net', 's365p005.in365.corpintra.net', 's365p006.in365.corpintra.net', 's365p007.in365.corpintra.net', 's365p008.in365.corpintra.net'],
# '2023-08-07 06:50:46_DEESIKR (local)': ['s365aid1lp203.apac.corpdir.net'],
# '2024-07-12 06:51:03_DWKRISH (local)': ['S365AID1SA197.in365.tbintra.net', 's365mid1s045.in365.corpintra.net'],
'Pushparaj, Nirmal': ['s365ald1te304.in365.lia.corpintra.net', 's365bid1te207.in365.corpintra.net', 's365ild1te085.in365.lia.corpintra.net'],
'Kumar V, Arun': ['s365ald1vlmi135.in365.lia.corpintra.net', 's365ild1vlmi064.in365.lia.corpintra.net'],
'Ronold, Mario': ['s365bid1b053.in365.corpintra.net', 's365iid1b032.in365.corpintra.net'],
'TATA, Sundravadanam': ['S365BID1P052.in365.corpintra.net', 's365ild1p019.in365.lia.corpintra.net', 't365bid1infr123.in365.corpintra.net'],
'D, Karthikeyan': ['S365BID1XW175.in365.tbintra.net'],
'Ramamurthy, Swarna': ['s365m004.in365.corpintra.net', 's365m155.in365.corpintra.net'],
'Pradheepan, Sam': ['s365m181.in365.corpintra.net'],
'Bal, Sangramkishor': ['s365mid1c051.in365.corpintra.net', 's365mid1c052.in365.corpintra.net', 's365mid1cctv053.in365.corpintra.net', 's365mid1cctv056.in365.corpintra.net', 's365mid1cctv057.in365.corpintra.net', 's365mid1cctv058.in365.corpintra.net', 's365mid1cctv059.in365.corpintra.net', 's365mid1cctv060.in365.corpintra.net', 's365mid2c050.in365.corpintra.net'],
'R S, Ezhilarasan': ['s365mid1f044.in365.corpintra.net'],
}

# Define email addresses for server owners
email_addresses = {
'Jeevan, Gopikrishnan': "gopikrishnan.jeevan@daimlertruck.com",
'S, Seetharaman': 'seetharaman.s@daimlertruck.com',
'Ss, Manojkumar':'manojkumar.ss@daimlertruck.com',
'M, Rajeshwaran': 'rajeshwaran.m@daimlertruck.com',
'Jacob, Joy': 'joy.jacob@daimlertruck.com',
'Marimuthu, Mathusuthanan': 'mathusuthanan.marimuthu@daimlertruck.com',
'Rangarajan, Srikanth': 'srikanth.rangarajan@daimlertruck.com',
'Mohana Sundaram, P': 'tataelxsi.mohana_sundaram@daimlertruck.com',
'Raja, Ravi Kumar': 'ravi_kumar.raja@daimlertruck.com',
'Sankar, K': "k.sankar@daimlertruck.com",
'K, Vikram': 'vikram.k@daimlertruck.com',
'S, Siva': 'siva.s@daimlertruck.com',
'M, Manjunatha': 'manjunatha.m@daimlertruck.com',
'Mohan, Sunantha': 'sunantha.mohan@daimlertruck.com',
'Kumar, Hemanth': 'hemanth.kumar@daimlertruck.com',
'P, Aravind': 'aravind.p@daimlertruck.com',
'V, Jaivinoth': 'jaivinoth.v@daimlertruck.com',
'Kevin Kenneth, Pakkiadoss': 'tata.kevin_kenneth@daimlertruck.com',
'Sridharan, S': 's.sridharan@daimlertruck.com',
'TATA, Sundravadanam':'sundravadanam.tata@daimlertruck.com',
'Rangarajan, Srikanth': "srikanth.rangarajan@daimlertruck.com",
'Pushparaj, Nirmal': 'nirmal.pushparaj@daimlertruck.com',
'Kumar V, Arun': 'arun.kumar_v@daimlertruck.com',
'Ronold, Mario': 'mario.ronold@daimlertruck.com',
'D, Karthikeyan': 'karthikeyan.d@daimlertruck.com',
'Ramamurthy, Swarna': 'swarna.ramamurthy@daimlertruck.com',
'Pradheepan, Sam': 'sam.pradheepan@daimlertruck.com',
'Bal, Sangramkishor': 'kishor.bal@daimlertruck.com',
'R S, Ezhilarasan': 'ezhilarasan.r_s@daimlertruck.com',
'Vairavan, Vinoth': 'vinoth.vairavan@daimlertruck.com',
'Sankar, K': 'k.sankar@daimlertruck.com',
'Kanagasabai, Saravanan': 'saravanan.s1.k@daimlertruck.com',
}

# Function to read and return the Excel data without scope check
def filter_scope_and_save_excel(input_file): 
    print("Reading the Excel file from the specified sheet")
    df = pd.read_excel(input_file, sheet_name="Sheet1", header=0)
    print("Stripping any leading/trailing whitespace characters from the column names")
    df.columns = df.columns.str.strip()
    return df  # Directly return the DataFrame without filtering by scope

# Function to filter by hostname and save per owner
def filter_hostname_and_save(input_file, email_template):
    df = filter_scope_and_save_excel(input_file)
    if 'DeviceName' not in df:
        print("Column 'DeviceName' not found in the data.")
        print(f"Available columns are: {df.columns.tolist()}")
        return

    current_date = datetime.datetime.now()
    year_suffix = current_date.strftime("%y")
    base_name = os.path.basename(input_file)
    name_part = "linux" if "linux" in base_name.lower() else "windows" if "windows" in base_name.lower() else "Windows_or_Linux"
    owner_dfs = {owner: pd.DataFrame(columns=df.columns) for owner in server_owners.keys()}

    for owner, hostnames in server_owners.items():
        for hostname in hostnames:
            filtered_data = df[df['DeviceName'].str.contains(hostname, na=False)]
            if not filtered_data.empty:
                owner_dfs[owner] = pd.concat([owner_dfs[owner], filtered_data])
    for owner, df in owner_dfs.items():
        if not df.empty:
            file_name = f"{owner}_Daimler_{name_part}_VMR_Oct_{year_suffix}.xlsx"
            df.to_excel(file_name, index=False)
            print(f"Data for {owner} saved to {file_name}")
            send_email_with_attachment(email_addresses[owner], file_name, owner, email_template)

# Function to read the HTML email template
def read_html_template(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='latin-1') as file:
            content = file.read()
    return content

# Function to send an email with attachment
def send_email_with_attachment(recipient_email, attachment_path, owner, email_template):
    outlook = win32.Dispatch('outlook.application')
    email_body = read_html_template(email_template)
    full_attachment_path = rf"C:\Users\KevinKennethPakkiado\OneDrive - Daimler Truck\Documents\Soc_Automation_Scripts\{attachment_path}"
    current_month = "Nov"
    current_year = "2024"
    subject = f"Vulnerability Report and Required Remediation Actions for {current_month} {current_year}"
    email_body = re.sub(r'{MONTH}', current_month, email_body)
    email_body = re.sub(r'{NAME}', owner, email_body)

    mail = outlook.CreateItem(0)
    mail.Display()
    mail.To = recipient_email
    mail.cc = "KPAKKIA;KSANKA;YUSEKAR;SARAVK5;dicv_itsecurity@daimlertruck.com"
    mail.Subject = subject
    mail.HTMLBody = email_body
    mail.Attachments.Add(full_attachment_path)
    mail.Importance = 2
    mail.SentOnBehalfOfName = 'dicv_itsecurity@daimlertruck.com'
   
    print(f"Email sent to {recipient_email} with attachment {attachment_path}")

# Define input files and templates
input_file = '25112024_Software Vulnerability List.xlsx'
email_template = "VM_template.htm"  
filter_hostname_and_save(input_file, email_template)