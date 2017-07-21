<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="CJDefault.aspx.cs" Inherits="ChallengeSimpleCalculator.CJDefault" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
    <style type="text/css">
        h1 {
            font-family: Arial, Helvetica, sans-serif;
            font-size: x-large;
        }
        .newStyle1 {
            font-family: Arial, Helvetica, sans-serif;
        }
        .newStyle2 {
            font-family: Arial, Helvetica, sans-serif;
        }
        .newStyle3 {
            font-family: Arial, Helvetica, sans-serif;
        }
    </style>
</head>
<body>
    <form id="form1" runat="server">
    <div style="font-family: Arial, Helvetica, sans-serif">
    
        <h1><span class="newStyle3">Simple Calculator</span></h1>
        <span class="newStyle1">&nbsp;First Value</span>:&nbsp;
        <asp:TextBox ID="FirstTextBox" runat="server"></asp:TextBox>
        <br />
        <br />
        <span class="newStyle2">Second Value:</span>&nbsp;
        <asp:TextBox ID="SecondTextBox" runat="server"></asp:TextBox>
        <br />
        <br />
        <br />
        <asp:Button ID="AddButton" runat="server" Font-Bold="True" OnClick="AddButton_Click" Text="+" Width="33px" />
&nbsp;&nbsp;&nbsp;&nbsp;
        <asp:Button ID="SubButton" runat="server" Font-Bold="True" OnClick="SubButton_Click" Text="-" Width="33px" />
&nbsp;&nbsp;&nbsp;&nbsp;
        <asp:Button ID="MulitButton" runat="server" Font-Bold="True" OnClick="MulitButton_Click" Text="*" Width="31px" />
&nbsp;&nbsp;&nbsp;&nbsp;
        <asp:Button ID="DivButton" runat="server" Font-Bold="True" OnClick="DivButton_Click" Text="/" Width="32px" />
        <br />
        <br />
        <br />
        <asp:Label ID="resultLabel" runat="server" BackColor="#6699FF" Font-Bold="True" Font-Size="Larger"></asp:Label>
    
    </div>
    </form>
</body>
</html>
