from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from proposals.models import AdditionalSpeaker, TalkProposal, TutorialProposal


class AdditionalSpeakerInline(GenericTabularInline):
    model = AdditionalSpeaker
    fields = ['user', 'status', 'cancelled']
    readonly_fields = ['user']
    ct_field = 'proposal_type'
    ct_fk_field = 'proposal_id'
    extra = 0


class ProposalAdmin(admin.ModelAdmin):

    fields = [
        'submitter', 'title', 'category', 'duration', 'language',
        'target_audience', 'abstract', 'python_level', 'objective',
        'detailed_description', 'outline', 'supplementary',
        'recording_policy', 'slide_link', 'cancelled',
    ]
    readonly_fields = ['submitter']
    search_fields = ['title', 'abstract']
    inlines = [AdditionalSpeakerInline]

    def has_add_permission(self, request):
        # Disable proposal submission via admin. Always use the public form!
        return False


@admin.register(TalkProposal)
class TalkProposalAdmin(ProposalAdmin):
    list_display = [
        'title', 'category', 'duration', 'language', 'target_audience',
        'python_level',
    ]
    list_filter = [
        'category', 'duration', 'language', 'target_audience', 'python_level',
    ]


@admin.register(TutorialProposal)
class TutorialProposalAdmin(ProposalAdmin):
    list_display = [
        'title', 'category', 'language', 'target_audience', 'python_level',
    ]
    list_filter = [
        'category', 'language', 'target_audience', 'python_level',
    ]
