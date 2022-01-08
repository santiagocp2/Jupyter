# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SurveySignature(models.Model):
    _inherit = 'survey.question'

    question_type = fields.Selection(selection_add=[("binary","Upload")])
    

class SurveySignatureInput(models.Model):
    _inherit = 'survey.user_input.line'

    answer_type = fields.Selection(selection_add=[("binary","Free Text")])
    signature=fields.Binary()



<odoo>
    <record model="ir.ui.view" id="survey_question_signature">
        <field name="name">survey.question.form</field>
        <field name="model">survey.question</field>
        <field name="inherit_id" ref="survey.survey_question_form"/>     
        <field name="arch" type="xml">
            <xpath expr="//div[@class='col-lg-6 offset-lg-3 o_preview_questions']" position="inside">
                <!-- Signature Zone -->
                <div attrs="{'invisible': [('question_type', '!=', 'binary')]}">
                    <i title="Signature" class='fa fa-pencil fa-4x' role="img" aria-label="Signature" />
                </div>           
            </xpath> 
        </field>
    </record>
    <record id="survey_user_input_line_view_form_signature" model="ir.ui.view">
        <field name="name">survey.user_input.line.view.form</field>
        <field name="model">survey.user_input.line</field>
        <field name="inherit_id" ref="survey.survey_user_input_line_view_form"/>
        <field name="arch" type="xml">
            <xpath expr="//field[@name='value_char_box']" position="before">
                <field name="signature" widget="signature" colspan='2' attrs="{'invisible': [('answer_type','!=','binary')]}"/>
            </xpath> 
        </field>
    </record>
</odoo>

from . import survey_signature

'views/survey_signature_view.xml',







