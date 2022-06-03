def add_time(start, duration, starting_day=False):

  days_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
  
  i = 0
  
  #Splitting start and getting values
  start_split = start.split(":")
  start_split_2 = start_split[1].split(" ")
  start_hours = start_split[0]
  start_minutes = start_split_2[0]
  am_or_pm = start_split_2[-1]
  
  #Splitting duration and getting values
  duration_split = duration.split(":")
  duration_hours = duration_split[0]
  duration_minutes = duration_split[1]
  
  days = 0
  
  added_minutes = int(start_minutes) + int(duration_minutes)
  
  added_hours = (int(start_hours) + int(duration_hours))
  added_hours2 = added_hours % 12
  
  if (added_minutes) >= 60:
      added_minutes -= 60
      added_hours += 1
      added_hours2 += 1
      
  if added_hours2 == 0:
      added_hours2 += 12
      
  am_pm_flip = added_hours // 12
  if (am_pm_flip) % 2 != 0:
      if(am_or_pm) == "PM":
          am_or_pm = "AM"
          days += 1
      elif(am_or_pm == "AM"):
          am_or_pm = "PM"
  
  days_passed = int(duration_hours) // 24
  
  days = days + days_passed
  days_loop = days
  
  final_day = ""
  
  returnTime = str(added_hours2) + ":" + "{:02d}".format(added_minutes) + " " + am_or_pm
  
  if(starting_day):
    index = days_week.index(starting_day.lower())
    if days > 0:
        i = index
        while i < 7:
            if (days_loop <= 0):
                break
            if (i == 6):
              i = 0
              days_loop -= 1
              continue
            i += 1
            days_loop -= 1
    
    final_day = days_week[i]
    returnTime += ", " + final_day.capitalize()
  
  if days == 1:
      return returnTime + " " + "(next day)"
      
  elif days > 1:
      return returnTime + " (" + str(days) + " days later)"
      
  else:
      return returnTime