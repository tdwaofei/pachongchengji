# coding: utf-8

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkocr.v1.region.ocr_region import OcrRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkocr.v1 import *

if __name__ == "__main__":
    ak = "8TZ6BMUOMWO9BORZI0GG"
    sk = "2bFlDAwKF7zidUYHOzUfnoTuI3hKDOwyp7ClLgAt"

    credentials = BasicCredentials(ak, sk)  # 替换为实际的AK和SK

    client = OcrClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(OcrRegion.value_of("cn-north-4")) \
        .build()

    try:
        request = RecognizeGeneralTextRequest()
        request.body = GeneralTextRequestBody(
            image="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"
        )
        response = client.recognize_general_text(request)
        print(response)
        response_dict = response.to_dict()
        words = response_dict['result']['words_block_list'][0]['words']
        print(words)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)
