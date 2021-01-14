#Import Module
import groupdocs_conversion_cloud as gcc


app_sid = "700b82a3-5416-48cf-9945-cd41f111116c"
app_key = "6bde0ca47399b6a7a2af4952b59c6fc3"

#Create an instance of the API

convert_api = gcc.ConvertApi.from_keys(app_sid, app_key)
file_api = gcc.FileApi.from_keys(app_sid, app_key)

try:
	#upload source file to storage
	filename = "StudentReport.pdf"
	remote_name = "StudentReport.pdf"
	output_name = "StudentReport.docx"
	strformat = "docx"
	request_upload = gcc.UploadFileRequest(remote_name, filename)
	response_upload = file_api.upload_file(request_upload)

	#Extract Text from PDF document
	settings = gcc.ConvertSettings()
	settings.file_path = remote_name
	settings.format = strformat
	settings.output_path = output_name
	request = gcc.ConvertDocumentRequest(settings)
	response = convert_api.convert_document(request)

	print("Document converted successfully: " + str(response))

except gcc.ApiException as e:
	print("Exception when calling get_supported_conversion_types: {0}".format(e.message))