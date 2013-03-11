namespace MvcTagBuilderIsNotXHTMLCompliant
{
    using System.Collections.Generic;
    using System.Web.Mvc;
    using System.Xml.Linq;

    using NUnit.Framework;

    [TestFixture]
    public class MvcTagBuilderXHTMLCompliancyTest
    {
        [Test]
        public void When_Setting_TagName_Property_Must_Be_All_Lower_Case()
        {
            TagBuilder builder = new TagBuilder("DIV");
            
            Assert.AreEqual("div", builder.TagName);
        }

        [Test]
        public void When_Tag_Is_Rendered_TagName_Must_Be_All_Lower_Case()
        {
            TagBuilder builder = new TagBuilder("DIV");

            string rendered = builder.ToString();

            XElement divElement = XElement.Parse(rendered);
            Assert.AreEqual("div", divElement.Name.LocalName);
        }

        [Test]
        public void AddCssClass_Must_Add_Class_Attribute_Lower_Case()
        {
            TagBuilder builder = new TagBuilder("div");

            builder.AddCssClass("someClass");
            string className = builder.Attributes["class"];
            
            Assert.AreEqual("someClass", className);
        }

        [Test]
        public void Attributes_Dictionary_Must_Add_Attribute_Lower_Case()
        {
            TagBuilder builder = new TagBuilder("div");

            builder.Attributes.Add("CLASS", "someClass");
            string className = builder.Attributes["class"];

            Assert.AreEqual("someClass", className);
        }

        [Test]
        public void After_Adding_Attributes_When_Tag_Is_Rendered_Attributes_Must_Be_All_Lower_Case()
        {
            TagBuilder builder = new TagBuilder("div");
            builder.Attributes.Add("CLASS", "someClass");

            string rendered = builder.ToString();

            XElement divElement = XElement.Parse(rendered);
            Assert.AreEqual("class", divElement.FirstAttribute.Name.LocalName);
        }

        [Test]
        public void After_Merging_Attributes_When_Tag_Is_Rendered_Attributes_Must_Be_All_Lower_Case()
        {
            TagBuilder builder = new TagBuilder("div");
            builder.MergeAttributes(
                new Dictionary<string, object>() 
                { { "CLASS", "someClass" } }
            );

            string rendered = builder.ToString();

            XElement divElement = XElement.Parse(rendered);
            Assert.AreEqual("class", divElement.FirstAttribute.Name.LocalName);
        }
    }
}