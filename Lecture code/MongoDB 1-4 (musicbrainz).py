q1 = query_by_name(ARTIST_URL, query_type["simple"], "FIRST AID KIT")
q1_count = 0
for artist in q1["artist"]:
    if artist["score"] == "100":
        q1_count += 1
print "Q1: Number of bands 'FIRST AID KIT' that had score == 100"
print q1_count

q2 = query_by_name(ARTIST_URL, query_type["simple"], "Queen")
begin_area = q2["artist"][0]["begin-area"]["name"]
print "Q2: Begin area for Queen"
print begin_area

q3 = query_by_name(ARTIST_URL, query_type["simple"], "Beatles")
aliases = q3["artist"][0]["aliases"]
for a in aliases:
    if a["locale"] == "es":
        alias = a["name"]
print "Q3: Spanish alias for Beatles"
print alias
#pretty_print(q3)

q4 = query_by_name(ARTIST_URL, query_type["simple"], "Nirvana")
disam = q4["artist"][0]["disambiguation"]
print "Q4: Disambiguation Nirvana"
print disam

q5 = query_by_name(ARTIST_URL, query_type["simple"], "One Direction")
begin_date = q5["artist"][0]["life-span"]["begin"]
print "Q5: One Direction begin"
print begin_date