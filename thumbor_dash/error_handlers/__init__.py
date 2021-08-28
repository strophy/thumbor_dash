
class Error(Exception):
    '''Base exception class'''
    pass

class BadRequestError(Error):
    '''The syntax was not respected'''
    pass

class UnauthorizedUserError(Error):
    '''The user does not exist'''
    pass

class PaymentError(Error):
    '''Not enough funds on identity'''
    pass

class ForbiddenSignatureError(Error):
    '''The signature is incorrect'''
    pass

class UnsupportedMediaTypeError(Error):
    '''The media type specified in the request is not supported'''
    pass

class TooManyRequestsError(Error):
    '''Client is temporarily banned'''
    pass

class DashPlatformError(Error):
    ''' An error occured with the dash platform service'''
    pass

class UnsignedURLError(Error):
    '''URL is not signed'''
    pass

class UnsafeURLError(Error):
    '''URL has unsafe but unsafe is not allowed '''
    pass

class UnspecifiedImageError(Error):
    '''No original image was specified'''
    pass

class BlacklistedSourceError(Error):
    '''Source image url has been blacklisted'''
    pass
