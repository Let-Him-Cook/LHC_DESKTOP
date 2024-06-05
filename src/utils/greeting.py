from datetime import datetime

def greeting():
  now = datetime.now()

  if now.hour < 12:
    return "Bom Dia"
  elif now.hour < 18:
    return "Boa Tarde"
  else:
    return "Boa Noite"