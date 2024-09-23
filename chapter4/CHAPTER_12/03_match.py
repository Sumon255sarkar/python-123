def http_status(status):
    match status:
        case 200 :
            return "Ok"
        case 300:
            return "Not Found "
        case 400 :
            return "International "
        case _:
            return "Unkown status "
        
print (http_status(200))
print (http_status(300))
print (http_status(400))
print (http_status(500))