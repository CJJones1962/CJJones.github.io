using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace ChallengeSimpleCalculator
{
    public partial class CJDefault : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {

        }

        protected void AddButton_Click(object sender, EventArgs e)
        {
            int FirstValue = int.Parse(FirstTextBox.Text);
            int SecondValue = int.Parse(SecondTextBox.Text);
            int result = FirstValue + SecondValue;
            resultLabel.Text = result.ToString();
        }

        protected void SubButton_Click(object sender, EventArgs e)
        {
            int FirstValue = int.Parse(FirstTextBox.Text);
            int SecondValue = int.Parse(SecondTextBox.Text);
            int result = FirstValue - SecondValue;
            resultLabel.Text = result.ToString();
        }

        protected void MulitButton_Click(object sender, EventArgs e)
        {
            int FirstValue = int.Parse(FirstTextBox.Text);
            int SecondValue = int.Parse(SecondTextBox.Text);
            int result = FirstValue * SecondValue;
            resultLabel.Text = result.ToString();
        }

        protected void DivButton_Click(object sender, EventArgs e)
        {
            double FirstValue = double.Parse(FirstTextBox.Text);
            double SecondValue = double.Parse(SecondTextBox.Text);
            double result = FirstValue / SecondValue;
            resultLabel.Text = result.ToString();
        }
    }
}