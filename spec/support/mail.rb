require "mail"
# require "colorize"

Mail.defaults do
  retriever_method :imap, { :address => "imap.googlemail.com",
                            :port => 993,
                            :user_name => "rtassessment@gmail.com",
                            :password => "!f33db@ck!",
                            :enable_ssl => true }
end

def clear_inbox
  Mail.all(delete_after_find: true)
end

def email_confirmation

end

