def extract_info(hospitals):
  result = []
  for coronoa_info in hospitals:

      city = hospital.find_all("td")[0].string
      district = hospital.find_all("td")[1].string
      hospital = hospital.find_all("td")[2].string
      contact = hospital.find_all("td")[3].string

    hospital_info = {
        "city" : city
        "district" : district
        "hospital" : hospital
        "contact" : contact
    }

    result.append(hospital_info)

  return result