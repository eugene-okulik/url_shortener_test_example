class Endpoint:
    short_url = None
    status_code = None
    response_body = None

    def response_is_200(self) -> bool:
        return self.status_code == 200

    def response_is_404(self) -> bool:
        return self.status_code == 404
