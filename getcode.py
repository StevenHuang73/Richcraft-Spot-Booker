import imaplib
def get_code(user,password,imap_url):


    # Function to get email content part i.e its body part
    def get_body(msg):
        if msg.is_multipart():
            return get_body(msg.get_payload(0))
        else:
            return msg.get_payload(None, True)


    # Function to search for a key value pair
    def search(key, value, con):
        result, data = con.search(None, key, '"{}"'.format(value))
        return data


    # Function to get the list of emails under this label
    def get_emails(result_bytes):
        msgs = []  # all the email data are pushed inside an array
        for num in result_bytes[0].split():
            typ, data = con.fetch(num, '(RFC822)')
            msgs.append(data)

        return msgs




    # this is done to make SSL connection with GMAIL
    con = imaplib.IMAP4_SSL(imap_url)

    # logging the user in
    con.login(user, password)

    # calling function to check for email under this label
    con.select('Inbox')

    # fetching emails from this user "tu**h*****1@gmail.com"
    msgs = get_emails(search('FROM', 'noreply@frontdesksuite.com', con))

    # Uncomment this to see what actually comes as data
    # print(msgs)

    # Finding the required content from our msgs
    # User can make custom changes in this part to
    # fetch the required content he / she needs

    # printing them by the order they are displayed in your gmail
    # for msg in msgs[::-1]:
    for sent in msgs[-1]:
        if type(sent) is tuple:

            # encoding set as utf-8
            content = str(sent[1], 'utf-8')
            data = str(content)
            #
            #         # Handling errors related to unicodenecode
            try:
                indexstart = data.find("code is:")
                data2 = data[indexstart + 10: len(data)]
                indexend = data2.find("The code must be entered on")

                # printing the required content which we need
                # to extract from our email i.e our body
                number = data2[0: indexend].strip()
                #
                # start_index = number.index("Your verification code is:") + len("Your verification code is:")
                # end_index = number.index("Received")
                # print(start_index)
                # print(end_index)

            except UnicodeEncodeError as e:
                pass
        return number
    
