
Candidates = {"Decker": 5, "Alex": 2, "Dad": 4, "Mom": 2}
Max_Votes = 0
Draw_Counter = 0


for kCand in Candidates:
    if Max_Votes < Candidates[kCand]:
        Max_Votes = Candidates[kCand]
        Winner = kCand


for _, votes in Candidates.items():
    if votes == Max_Votes:
        Draw_Counter += 1

if Draw_Counter > 1:
    Result = "It's a DRAW"
else:    
    Result = Winner