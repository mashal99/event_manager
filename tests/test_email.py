import pytest
from unittest.mock import MagicMock
from app.services.email_service import EmailService
from app.models.user_model import User

@pytest.fixture
def mock_template_manager():
    from app.utils.template_manager import TemplateManager
    template_manager = MagicMock(spec=TemplateManager)
    template_manager.render_template.return_value = "<html>Mock Email Content</html>"
    return template_manager

@pytest.fixture
def mock_smtp_client():
    from app.utils.smtp_connection import SMTPClient
    smtp_client = MagicMock(spec=SMTPClient)
    return smtp_client

@pytest.fixture
def email_service(mock_template_manager, mock_smtp_client):
    service = EmailService(template_manager=mock_template_manager)
    service.smtp_client = mock_smtp_client  # Inject mock SMTP client
    return service

@pytest.mark.asyncio
async def test_send_markdown_email(email_service, mock_smtp_client):
    user_data = {
        "email": "test@example.com",
        "name": "Test User",
        "verification_url": "http://example.com/verify?token=abc123"
    }

    # Call the method under test
    await email_service.send_user_email(user_data, 'email_verification')

    # Assert that the send_email method was called with the expected arguments
    mock_smtp_client.send_email.assert_called_once_with(
        "Verify Your Account",  # Subject
        "<html>Mock Email Content</html>",  # Rendered email content
        "test@example.com"  # Recipient email
    )
