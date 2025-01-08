from google.cloud import vision

feature = vision.Feature(type_=vision.Feature.Type.DOCUMENT_TEXT_DETECTION)
client = vision.ImageAnnotatorClient()


def pdf2txt(input: bytes) -> str:
    input_config = vision.InputConfig(content=input, mime_type="application/pdf")
    request = vision.AnnotateFileRequest(features=[feature], input_config=input_config)
    response = client.batch_annotate_files(requests=[request], timeout=50).responses[0]
    full_text = ""
    for image_response in response.responses:
        full_text += image_response.full_text_annotation.text + "\n"
    return full_text
