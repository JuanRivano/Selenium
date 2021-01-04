import pathlib
from Google import Create_Service
import io
import base64
import time


def construct_service(api_service):
    CLIENT_SERVICE_FILE = "client_secret.json"
    try:
        if api_service == "drive":
            API_NAME = "drive"
            API_VERSION = "v3"
            SCOPE = ['https://www.googleapis.com/auth/drive']
            return Create_Service(CLIENT_SERVICE_FILE, API_NAME, API_VERSION, SCOPE)
        elif api_service == 'gmail':
            API_NAME = "gmail"
            API_VERSION = "v1"
            SCOPE = ['https://mail.google.com/']
            return Create_Service(CLIENT_SERVICE_FILE, API_NAME, API_VERSION, SCOPE)
    except Exception as e:
        print(e)
        return None


def search_email(service, query_string, label_ids=[]):
    try:
        message_list_response = service.users().messages().list(
            userId='me',
            labelIds=label_ids,
            q=query_string
        ).execute()
        message_items = message_list_response.get('messages')
        nextPageToken = message_list_response.get('nextPageToken')

        while nextPageToken:
            message_list_response = service.users().messages().list(
                userId='me',
                labelIds=label_ids,
                q=query_string,
                pageToken=nextPageToken
            ).execute()
            message_items.extend(message_list_response.get('messages'))
            nextPageToken = message_list_response.get('nextPageToken')
        return message_items

    except Exception as e:
        return None


def get_message_detail(service, message_id, format='metadata', metadata_headers=[]):
    try:
        message_detail = service.users().messages().get(
            userId='me',
            id=message_id,
            format=format,
            metadataHeaders=metadata_headers
        ).execute()
        return message_detail

    except Exception as e:
        print(e)
        return None


def buscar_correo():
    while True:
        try:
            """
            step1: crear interface de servicio google
            """
            gmail_service = construct_service('gmail')
            time.sleep(2)
            drive_service = construct_service('drive')

            """
            Buscar en Gmail (con archivos adjuntos)
            """
            query_string = 'from:(OficinaInternet@srcei.cl) has:attachment after:2020/12/31'
            email_messages = search_email(gmail_service, query_string, ['INBOX'])
            """
            Step3 Descargar Emails y crear carpeta en Drive
            """
            for email_message in email_messages:
                messageId = email_message['threadId']
                messageSubject = '(No Subject)({0})'.format(messageId)
                messageDetail = get_message_detail(
                    gmail_service, email_message['id'],
                    format='full',
                    metadata_headers=['parts'])
                messageDetailPayload = messageDetail.get('payload')
                for item in messageDetailPayload['headers']:
                    if item['name'] == 'Subject':
                        if item['value']:
                            messageSubject = '{0} ({1})'.format(item['value'], messageId)
                    else:
                        messageSubject = '(No Subject)({0})'.format(messageId)
                if 'parts' in messageDetailPayload:
                    for msgPayload in messageDetailPayload['parts']:
                        mime_type = msgPayload['mimeType']
                        file_name = msgPayload['filename']
                        body = msgPayload['body']

                        if 'attachmentId' in body:
                            attachment_id = body['attachmentId']

                            response = gmail_service.users().messages().attachments().get(
                                userId='me',
                                messageId=email_message['id'],
                                id=attachment_id
                            ).execute()

                            file_data = base64.urlsafe_b64decode(
                                response.get('data').encode('UTF-8'))
                            fh = io.BytesIO(file_data)
                            pathlib.Path(f'pdf/{file_name}').write_bytes(fh.getbuffer())
            break
        except ValueError:
            print("Correo no encontrado")