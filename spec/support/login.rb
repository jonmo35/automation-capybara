require "capybara/rspec"

module LoginHelper
  class LoginUser
    def login_form(params = {})
      fill_in "CustomerEmail", with: params.fetch(:CustomerEmail)
      fill_in "CustomerPassword", with: params.fetch(:CustomerPassword)
      self
    end

    def login_button
      click_button("sign in")
      self
    end

    def login_qa_user
      login_form(
        login.login_form(
          CustomerEmail: "rtassessment@gmail.com",
          CustomerPassword: "!f33db@ck!",
        ).login_button
      )
    end
  end
end
