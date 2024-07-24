You are tasked with performing layout analysis on a UI screenshot to identify and locate various UI elements such as buttons, labels, images, and other specified components. This analysis is similar to document layout analysis but focuses on user interface elements.

You will be provided with a screenshot of a user interface and a list of element types to analyze. Your goal is to identify these elements in the image and provide their locations and basic properties.

Here is the screenshot to analyze:
<screenshot>
{{SCREENSHOT}}
</screenshot>

The element types you should look for are:
<element_types>
{{ELEMENT_TYPES}}
</element_types>

To perform the layout analysis:
1. Carefully examine the screenshot.
2. Identify all instances of the specified element types.
3. For each identified element:
   a. Determine its type (e.g., button, label, image)
   b. Estimate its location using x and y coordinates (assume the top-left corner of the image is 0,0)
   c. Estimate its width and height
   d. Note any other relevant properties (e.g., text content for labels, image description for images)

Provide your analysis results in the following format:
<analysis>
<element>
<type>Element Type</type>
<location>
  <x>X coordinate</x>
  <y>Y coordinate</y>
</location>
<size>
  <width>Width in pixels</width>
  <height>Height in pixels</height>
</size>
<properties>
  <property_name>Property Value</property_name>
  ...
</properties>
</element>
...
</analysis>

Here's an example of how your output might look:

<analysis>
<element>
<type>Button</type>
<location>
  <x>50</x>
  <y>100</y>
</location>
<size>
  <width>80</width>
  <height>30</height>
</size>
<properties>
  <text>Submit</text>
  <color>Blue</color>
</properties>
</element>
<element>
<type>Label</type>
<location>
  <x>20</x>
  <y>50</y>
</location>
<size>
  <width>100</width>
  <height>20</height>
</size>
<properties>
  <text>Enter your name:</text>
</properties>
</element>
</analysis>

Remember to be as accurate as possible in your estimations of locations and sizes. If you're unsure about a particular element or property, you can indicate this in your analysis.

Begin your analysis now, and provide your results within <analysis> tags as shown in the example above.
