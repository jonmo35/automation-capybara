require "capybara/rspec"

module CreateAccount
  class AccountForm
    include Capybara::DSL

    def create_new_account
      within("#CustomerLoginForm") do
        find('a[href="/account/register"]').click
      end
      self
    end

    def submit
      click_button "sign up"
      self
    end

    def fill_in_with(params = {})
      fill_in "FirstName", with: params.fetch(:FirstName)
      fill_in "LastName", with: params.fetch(:LastName)
      fill_in "Email", with: params.fetch(:Email)
      fill_in "CreatePassword", with: params.fetch(:CreatePassword)
      self
    end

    def check_news_letter
      check "marketing"
      self
    end
  end
end
